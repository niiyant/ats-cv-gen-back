# Usa una imagen oficial de Python 3.12 como base
FROM python:3.12-slim

# Crear un usuario no root
RUN useradd -m appuser

# Instalar dependencias del sistema para psycopg2 (opcional si usas psycopg2-binary)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
    
# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    postgresql-client \  
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

ENV AZUREML_EXTRA_REQUIREMENTS_TXT requirements.txt
# Copiar e instalar dependencias de Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Copiar el script de espera para PostgreSQL
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
RUN chmod +x /app/wait-for-postgres.sh

# Cambiar al usuario no root
USER appuser

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["./wait-for-postgres.sh", "postgres_db", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]