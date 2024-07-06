
# Aplicación de Lista de Tareas

Esta es una aplicación simple de lista de tareas creada con Flask. Permite agregar, ver, editar y eliminar tareas.

## Funcionalidades

- **Ver Tareas**: Muestra una lista de todas las tareas.
- **Agregar Tarea**: Permite agregar una nueva tarea con título y descripción.
- **Editar Tarea**: Permite editar el título y la descripción de una tarea existente.
- **Eliminar Tarea**: Permite eliminar una tarea de la lista.
- **Marcar Tarea como Completada**: Permite marcar una tarea como completada usando una casilla de verificación.
- **Eliminar Tareas Completadas**: Permite eliminar todas las tareas completadas después de confirmar en un modal.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `models.py`: Archivo que define el modelo de datos para las tareas utilizando SQLAlchemy.
- `templates/`: Directorio que contiene las plantillas HTML.
  - `index.html`: Plantilla para mostrar la lista de tareas.
  - `agregar.html`: Plantilla para agregar una nueva tarea.
  - `editar.html`: Plantilla para editar una tarea existente.
- `static/css/styles.css`: Archivo CSS generado por TailwindCSS para los estilos de la aplicación.

## Cómo Ejecutar la Aplicación Localmente

1. Asegúrate de tener [pip](https://pip.pypa.io/en/stable/) instalado.
2. Clona este repositorio.
3. Navega al directorio del proyecto.
4. Instala las dependencias utilizando pip:

   ```sh
   pip install -r requirements.txt
   ```

5. Genera el archivo CSS de Tailwind:

   ```sh
   npx tailwindcss build static/css/tailwind.css -o static/css/styles.css
   ```

6. Ejecuta la aplicación Flask:

   ```sh
   flask run
   ```

7. Abre tu navegador web y ve a `http://127.0.0.1:5000` para ver la aplicación en acción.

## Cómo Ejecutar la Aplicación con Docker

1. Asegúrate de tener [Docker](https://www.docker.com/) instalado.
2. Construye la imagen de Docker:

   ```sh
   docker build -t todo-app .
   ```

3. Ejecuta el contenedor de Docker:

   ```sh
   docker run -p 5000:5000 todo-app
   ```

4. Abre tu navegador web y ve a `http://127.0.0.1:5000` para ver la aplicación en acción.

## Requisitos

- Python 3.10 o superior
- Flask 3.0.3
- Flask-SQLAlchemy 3.1.1
- SQLAlchemy 2.0.31
- TailwindCSS
- Docker (para la ejecución con Docker)

