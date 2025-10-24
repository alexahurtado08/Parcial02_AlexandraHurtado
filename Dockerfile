
FROM python:3.10-slim

# directorio de trabajo
WORKDIR /app

# instalar dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar el codigo
COPY . .

# Exponer el puerto 8080
EXPOSE 8080

# ejecutar la aplicacion
CMD ["python", "app.py"]
