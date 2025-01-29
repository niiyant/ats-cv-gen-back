# Usa una imagen oficial de Python específica y ligera
FROM python:3.12-slim

# Crear un usuario no root para mayor seguridad
RUN useradd -m appuser

# Instalar dependencias del sistema para psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar solo el archivo de requerimientos para aprovechar el cache
COPY requirements.txt requirements.txt

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar solo los archivos necesarios
COPY . .

# Copiar el script de espera para PostgreSQL
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
RUN chmod +x /app/wait-for-postgres.sh

# Cambiar al usuario no root
USER appuser

# Exponer el puerto donde correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["./wait-for-postgres.sh", "postgres_db", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
