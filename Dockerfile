# Utiliza la imagen base de Python
FROM python:3.10.12-alpine3.17

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala virtualenv y crea un entorno virtual
RUN pip install virtualenv
RUN virtualenv venv

# Activa el entorno virtual
ENV PATH="/app/venv/bin:$PATH"

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala los paquetes definidos en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia la aplicación Flask al directorio de trabajo en el contenedor
COPY /flask /app

# Expone el puerto 5000 (puedes cambiarlo según tus necesidades)
EXPOSE 5000

# Comando para ejecutar Gunicorn con la aplicación Flask
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]