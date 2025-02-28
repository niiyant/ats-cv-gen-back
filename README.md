# CV Generator API

Este proyecto es una API construida con FastAPI para la generación de CVs y autenticación de usuarios. La base de datos utilizada es PostgreSQL, y se encuentra dockerizada para facilitar su despliegue.

## Requisitos

- Docker y Docker Compose
- Python 3.12

## Instalación y ejecución

1. Clona el repositorio:

   ```bash
   git clone <repo-url>
   cd cv-generator
   ```

2. Crea un archivo `.env` basado en el archivo de ejemplo (En caso):
> **¡Importante!** Si estás haciendo con Docker salta este paso.

   ```bash
   cp .env.example .env
   ```

   Ajusta las variable de entorno según tu configuración.
   DATABASE_URL='postgresql://share_it_ats_user:10x5C.0_0T0N7@35.226.215.172:5432/share_it_ats'

3. Construye y levanta los contenedores:

   ```bash
   docker-compose up --build
   ```

4. Para detener los contenedores:
   ```bash
   docker-compose down
   ```

## Acceso a la API

Una vez que la aplicación esté en ejecución, puedes acceder a la documentación de la API en:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Acceso a la base de datos en la nube

Para conectarte a la base de datos PostgreSQL dentro del contenedor, usa el siguiente comando:

```bash
 docker exec -it postgres_db psql -U postgres -d mydatabase
```

También puedes conectarte desde tu máquina local usando herramientas como DBeaver o pgAdmin con la siguiente configuración:

- Host: `35.226.215.172`
- Puerto: `5432`
- Usuario: `share_it_ats_user`
- Contraseña: `10x5C.0_0T0N7`
- Base de datos: `share_it_ats`
  

## Migraciones de base de datos

Este proyecto utiliza Alembic para la gestión de migraciones de la base de datos de forma síncrona.

### Crear una nueva migración

```bash
docker exec -it fastapi_app alembic revision --autogenerate -m "descripcion de la migracion"
```

### Aplicar migraciones

```bash
docker exec -it fastapi_app alembic upgrade head
```

### Revertir última migracion

```bash
docker exec -it fastapi_app alembic downgrade -1
```

**Nota:** Como la base de datos está en la nube, cualquier migración afectará a todos los usuarios conectados.

## 📌 Logging en FastAPI

En el desarrollo de aplicaciones, especialmente en entornos productivos, es fundamental llevar un registro detallado de eventos, advertencias y errores.  

El uso de `logger` en lugar de simples impresiones `print()` nos permite:

✔ Mantener un registro estructurado de lo que sucede en la aplicación.  
✔ Definir niveles de importancia para los mensajes (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).  
✔ Guardar logs en archivos para análisis posterior.  
✔ Integrarse con sistemas externos de monitoreo y depuración.  

Al implementar un `logger` personalizado en FastAPI, podemos controlar y registrar eventos de manera eficiente sin afectar el rendimiento ni la legibilidad del código.  


```python
from src.logger_config import logger

logger.debug("Para depuración detallada")
logger.info("Información general")
logger.warning("Advertencias") 
logger.error("Errores que afectan la ejecución")
logger.critical("Errores graves")
```

### Ejemplo:

```python
from src.logger_config import logger

logger.info(f"Token: {token}")
```

#### Output
```bash
fastapi_app  | INFO: ->  [security.py:40] msg:" Token: eyJhbGciOiJIUzI... " 23:23:45
```

## Autor

Desarrollado por SharedIt - 2025.
