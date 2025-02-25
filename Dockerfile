# Define la imagen base para el contenedor.
FROM python:3.9

#Define el directorio de trabajo dentro del contenedor.
WORKDIR /app

#Copia el archivo requirements.txt desde la PC anfitriona al contenedor.
COPY requirements.txt requirements.txt

#Instala las dependencias del archivo requirements.txt en el contenedor.
RUN pip install -r requirements.txt

#Copia el contenido del directorio actual de la PC anfitriona al directorio de trabajo del contenedor.
#una buena practica es utilizar un archivo .dockerignore para evitar copiar archivos innecesarios.
COPY . .

#Define el comando que se ejecutará cuando el contenedor inicie.
#Permite que el contenedor se ejecute automáticamente sin que el usuario tenga que ingresar comandos manualmente.
CMD ["python", "app.py"]