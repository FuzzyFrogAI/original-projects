import os
import random
import asyncio

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import boto3
from pymongo import MongoClient


class HelloCamera(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        self.photo = toga.ImageView(style=Pack(height=100, padding=5))
        camera_button = toga.Button(
            "Tomar foto",
            on_press=self.take_photo,
            style=Pack(padding=5)
        )

        self.message_label = toga.Label(
            "",
            style=Pack(padding=(10, 0), font_size=20, color='red')
        )

        self.plague_type_label = toga.Label(
            "Tipo de plaga: Desconocido",
            style=Pack(padding=(10, 0))
        )
        self.probability_label = toga.Label(
            "Probabilidad: 0%",
            style=Pack(padding=(5, 0))
        )
        self.description_label = toga.MultilineTextInput(
            value="Descripcion: N/A",
            readonly=True,
            style=Pack(padding=(5, 0), height=100)
        )
        self.advice_label = toga.MultilineTextInput(
            value="Consejos: N/A",
            readonly=True,
            style=Pack(padding=(5, 0), height=100)
        )

        main_box.add(self.photo)
        main_box.add(camera_button)
        main_box.add(self.message_label)
        main_box.add(self.plague_type_label)
        main_box.add(self.probability_label)
        main_box.add(self.description_label)
        main_box.add(self.advice_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        self.plague_data = {
                'Aphids': {
                    'nombre': 'Áfidos',
                    'descripcion': 'Insectos pequeños que se alimentan de savia de las plantas.',
                    'sugerencias': 'Usar insecticidas específicos o agua jabonosa para eliminarlos.'
                },
                'Army worm': {
                    'nombre': 'Gusano militar',
                    'descripcion': 'Oruga que ataca a diferentes cultivos.',
                    'sugerencias': 'Aplicar insecticidas o técnicas de manejo integrado de plagas.'
                },
                'Bacterial blight': {
                    'nombre': 'Tizón bacteriano',
                    'descripcion': 'Enfermedad bacteriana que afecta hojas, frutos o tallos.',
                    'sugerencias': 'Eliminar partes afectadas y aplicar fungicidas adecuados.'
                },
                'Cotton Boll Rot': {
                    'nombre': 'Pudrición del boll de algodón',
                    'descripcion': 'Enfermedad fúngica que afecta las estructuras reproductivas del algodón.',
                    'sugerencias': 'Aplicar fungicidas y mejorar las condiciones de ventilación.'
                },
                'Green Cotton Boll': {
                    'nombre': 'Boll de algodón verde',
                    'descripcion': 'Estado natural del boll de algodón antes de madurar.',
                    'sugerencias': 'Monitorear el desarrollo y proteger contra plagas.'
                },
                'Healthy': {
                    'nombre': 'Sano',
                    'descripcion': 'Estado de la planta libre de plagas y enfermedades.',
                    'sugerencias': 'Mantener prácticas de cultivo adecuadas y monitorear regularmente.'
                },
                'Powdery mildew': {
                    'nombre': 'Oídio',
                    'descripcion': 'Enfermedad fúngica que aparece como polvo blanco en hojas y tallos.',
                    'sugerencias': 'Usar fungicidas preventivos y mejorar la circulación de aire.'
                },
                'Target spot': {
                    'nombre': 'Mancha foliar',
                    'descripcion': 'Enfermedad que causa manchas circulares en hojas y frutos.',
                    'sugerencias': 'Eliminar hojas afectadas y usar fungicidas según las recomendaciones.'
                }
            }

    async def display_messages(self, messages):
        for i, message in enumerate(messages):
            self.message_label.text = message
            await asyncio.sleep(0.7)

    async def take_photo(self, widget, **kwargs):
        try:
            if not self.camera.has_permission:
                await self.camera.request_permission()

            image = await self.camera.take_photo()
            if image:
                self.photo.image = image

                # Mostrar diálogo de "Analizando, espere..."
                asyncio.create_task(self.display_messages(["Cargando imagen", "Analizando imagen", "Esperando resultados"]))

                # Detección de plaga
                plague_type, probability = await asyncio.to_thread(self.plague_detection, image)

                self.plague_type_label.text = f"Tipo de plaga: {self.plague_data[plague_type]['nombre']}"
                self.probability_label.text = f"Probabilidad: {probability}%"
                self.description_label.value = f"Descripcion: {self.plague_data[plague_type]['descripcion']}"
                self.advice_label.value = f"Consejos: {self.plague_data[plague_type]['sugerencias']}"

                self.message_label.text = ""

        except NotImplementedError:
            await self.main_window.info_dialog(
                "Oh no!",
                "La API de la cámara no está implementada en esta plataforma",
            )
        except PermissionError:
            await self.main_window.info_dialog(
                "Oh no!",
                "No has otorgado permiso para tomar fotos",
            )

    def plague_detection(self, image):
        """
        Sube la imagen a almacenamiento en la nube y consulta la base de
        datos hasta obtener el resultado escrito por el proceso de
        inferencia (fuera del alcance de este repositorio).

        Credenciales y endpoints se leen de variables de entorno, nunca
        deben quedar escritas directamente en el código. Configura un
        archivo .env local o las variables de entorno de tu sistema
        antes de correr la app:

            AWS_ACCESS_KEY_ID
            AWS_SECRET_ACCESS_KEY
            AWS_REGION
            S3_BUCKET_NAME
            MONGODB_URI
        """
        try:
            numero_aleatorio = random.randint(1000, 9999)

            s3 = boto3.client(
                's3',
                region_name=os.environ.get("AWS_REGION", "us-east-1"),
                aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
            )
            bucket_name = os.environ["S3_BUCKET_NAME"]
            s3.put_object(Bucket=bucket_name, Key=f"image_{numero_aleatorio}.jpg", Body=image.data)

            uri = os.environ["MONGODB_URI"]
            cliente = MongoClient(uri)
            base_de_datos = cliente['plaga']
            coleccion_plagas = base_de_datos['plagas_algodon']

            # Busca el resultado del análisis en la base de datos
            results = coleccion_plagas.find_one({"imageName": f"image_{numero_aleatorio}.jpg"})
            while not results:
                results = coleccion_plagas.find_one({"imageName": f"image_{numero_aleatorio}.jpg"})

        except Exception as e:
            print(f"Error al subir la imagen o consultar el resultado: {e}")
            return "Error", 0

        plague_type, probability = results['prediction'], results['probability']

        return plague_type, probability


def main():
    return HelloCamera()
