from pydantic_settings import BaseSettings

class AuthConfig(BaseSettings):
    SECRET_KEY: str = "tu-clave-secreta-segura-aqui"  # Cambiar esto en producción!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "postgresql://postgres:admin@postgres_db:5432/mydatabase"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


auth_config = AuthConfig()