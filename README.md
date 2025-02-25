# flask-crud-tareas

Este es un proyecto simple de API REST para la gestión de tareas utilizando **Flask**. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una lista de tareas en memoria.

## 📌 Requisitos

Asegúrate de tener instalado:
- **Python 3.9+**
- **Docker (opcional, si deseas ejecutar con contenedor)**

## 🚀 Instalación y Ejecución

### 🔹 Ejecutar localmente con Python

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu_usuario/flask-crud-tareas.git
   cd flask-crud-tareas
   ```
2. Crea un entorno virtual y actívalo:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```sh
   python app.py
   ```
5. Accede a la API en `http://127.0.0.1:5000/`

### 🔹 Ejecutar con Docker

1. Construye la imagen de Docker:
   ```sh
   docker build -t flask-crud-tareas .
   ```
2. Ejecuta el contenedor:
   ```sh
   docker run -p 5000:5000 flask-crud-tareas
   ```
3. Accede a la API en `http://localhost:5000/`

## 📌 Endpoints Disponibles

| Método   | Endpoint           | Descripción                      |
|----------|--------------------|----------------------------------|
| `GET`    | `/`                | Mensaje de bienvenida           |
| `GET`    | `/tareas`          | Listar todas las tareas         |
| `GET`    | `/tareas/<id>`     | Obtener una tarea específica    |
| `POST`   | `/tareas`          | Crear una nueva tarea           |
| `PUT`    | `/tareas/<id>`     | Editar una tarea existente      |
| `DELETE` | `/tareas/<id>`     | Eliminar una tarea              |

## 📂 Estructura del Proyecto

```
flask-crud-tareas/
│── app.py           # Archivo principal con las rutas de Flask
│── model.py         # Lógica de gestión de tareas
│── Dockerfile       # Configuración de Docker
│── requirements.txt # Dependencias del proyecto
│── README.md        # Documentación del proyecto
```

## 🛠️ Tecnologías Utilizadas
- **Flask** - Microframework para Python.
- **Docker** - Para ejecutar la aplicación en contenedor (opcional).

## 📜 Licencia
Este proyecto está bajo la licencia MIT.

---

✨ ¡Si te resulta útil este proyecto, no dudes en darle una ⭐ en GitHub!

