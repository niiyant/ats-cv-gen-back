#!/bin/bash
set -e

host="$1"
shift
cmd="$@"

until pg_isready -h "$host" -p 5432; do
  echo "Postgres no está listo en $host:5432. Esperando..."
  sleep 1
done

echo "Postgres está listo en $host:5432. Ejecutando el comando."
exec $cmd
