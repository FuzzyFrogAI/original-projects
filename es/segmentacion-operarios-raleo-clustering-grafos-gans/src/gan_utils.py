"""
gan_utils.py

Generador y discriminador reutilizables para una DCGAN simple sobre
imágenes en escala de grises de 28x28 (p. ej. MNIST como proxy, o
recortes de piezas de inspección visual reescalados a ese tamaño).

Uso típico:

    from src.gan_utils import construir_generador, construir_discriminador, entrenar_gan

    generador = construir_generador()
    discriminador = construir_discriminador()
    entrenar_gan(generador, discriminador, x_clase_minoritaria, epochs=30)
"""

from __future__ import annotations

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

LATENT_DIM = 100


def construir_generador(latent_dim: int = LATENT_DIM) -> tf.keras.Sequential:
    return tf.keras.Sequential([
        layers.Dense(7 * 7 * 128, use_bias=False, input_shape=(latent_dim,)),
        layers.BatchNormalization(),
        layers.LeakyReLU(0.2),
        layers.Reshape((7, 7, 128)),

        layers.Conv2DTranspose(64, 5, strides=1, padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(0.2),

        layers.Conv2DTranspose(32, 5, strides=2, padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(0.2),

        layers.Conv2DTranspose(1, 5, strides=2, padding="same", use_bias=False, activation="tanh"),
    ])


def construir_discriminador() -> tf.keras.Sequential:
    return tf.keras.Sequential([
        layers.Conv2D(32, 5, strides=2, padding="same", input_shape=(28, 28, 1)),
        layers.LeakyReLU(0.2),
        layers.Dropout(0.3),

        layers.Conv2D(64, 5, strides=2, padding="same"),
        layers.LeakyReLU(0.2),
        layers.Dropout(0.3),

        layers.Flatten(),
        layers.Dense(1),
    ])


_cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)


def _perdida_discriminador(salida_real, salida_falsa):
    perdida_real = _cross_entropy(tf.ones_like(salida_real), salida_real)
    perdida_falsa = _cross_entropy(tf.zeros_like(salida_falsa), salida_falsa)
    return perdida_real + perdida_falsa


def _perdida_generador(salida_falsa):
    return _cross_entropy(tf.ones_like(salida_falsa), salida_falsa)


def entrenar_gan(
    generador: tf.keras.Model,
    discriminador: tf.keras.Model,
    x_clase: np.ndarray,
    epochs: int = 30,
    batch_size: int = 64,
    latent_dim: int = LATENT_DIM,
    lr: float = 1e-4,
    verbose_cada: int = 5,
) -> tuple[list[float], list[float]]:
    """Entrena generador y discriminador en competencia sobre x_clase
    (imágenes normalizadas a [-1, 1], forma (N, 28, 28, 1)).

    Devuelve (historial_loss_generador, historial_loss_discriminador).
    """
    opt_generador = tf.keras.optimizers.Adam(lr)
    opt_discriminador = tf.keras.optimizers.Adam(lr)

    dataset = tf.data.Dataset.from_tensor_slices(x_clase).shuffle(1000).batch(batch_size)

    @tf.function
    def paso(imagenes_reales):
        ruido = tf.random.normal([tf.shape(imagenes_reales)[0], latent_dim])
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            imagenes_generadas = generador(ruido, training=True)
            salida_real = discriminador(imagenes_reales, training=True)
            salida_falsa = discriminador(imagenes_generadas, training=True)

            loss_gen = _perdida_generador(salida_falsa)
            loss_disc = _perdida_discriminador(salida_real, salida_falsa)

        grad_gen = gen_tape.gradient(loss_gen, generador.trainable_variables)
        grad_disc = disc_tape.gradient(loss_disc, discriminador.trainable_variables)

        opt_generador.apply_gradients(zip(grad_gen, generador.trainable_variables))
        opt_discriminador.apply_gradients(zip(grad_disc, discriminador.trainable_variables))
        return loss_gen, loss_disc

    hist_gen, hist_disc = [], []
    for epoch in range(epochs):
        perdidas_gen, perdidas_disc = [], []
        for batch in dataset:
            lg, ld = paso(batch)
            perdidas_gen.append(float(lg))
            perdidas_disc.append(float(ld))

        hist_gen.append(float(np.mean(perdidas_gen)))
        hist_disc.append(float(np.mean(perdidas_disc)))

        if (epoch + 1) % verbose_cada == 0 or epoch == 0:
            print(f"Epoch {epoch + 1}/{epochs} | loss_gen={hist_gen[-1]:.3f} | loss_disc={hist_disc[-1]:.3f}")

    return hist_gen, hist_disc


def generar_imagenes(generador: tf.keras.Model, n: int = 16, latent_dim: int = LATENT_DIM) -> np.ndarray:
    """Genera n imágenes sintéticas en escala de grises (0-255, uint8, HxW)."""
    ruido = tf.random.normal([n, latent_dim])
    imagenes = generador(ruido, training=False)
    imagenes = (imagenes.numpy() * 127.5 + 127.5).astype("uint8")
    return imagenes.reshape(n, imagenes.shape[1], imagenes.shape[2])
