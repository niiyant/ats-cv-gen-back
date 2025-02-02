#!/bin/sh

host="postgres_db"
port="5432"
timeout=30
retry_interval=2

echo "Esperando a PostgreSQL en $host:$port..."

for i in $(seq 1 $max_retries); do
    if pg_isready -h $host -p $port; then
        echo "PostgreSQL está listo."
        exit 0
    fi
    echo "Intento $i/$max_retries: PostgreSQL no está listo. Esperando..."
    sleep $retry_interval
done

echo "¡Error: PostgreSQL no está listo después de $max_retries intentos!"
exit 1