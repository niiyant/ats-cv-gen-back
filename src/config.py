from pydantic_settings import BaseSettings # BaseSettings es una clase base que permite cargar y validar configuraciones desde variables de entorno o archivos.

# Define una clase llamada AuthConfig que hereda de BaseSettings.
# Esta clase se utiliza para almacenar y gestionar configuraciones relacionadas con la autenticación.
class AuthConfig(BaseSettings):
    SECRET_KEY: str = "tu-clave-secreta-segura-aqui"  # Cambiar esto en producción!
    ''' Esta clave secreta se utiliza para firmar y verificar tokens JWT.'''
    ALGORITHM: str = "HS256"
    ''' Especifica el algoritmo utilizado para firmar los tokens JWT (en este caso, HS256) '''
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ''' Especifica el tiempo de expiración (en minutos) de los tokens de acceso JWT.'''
    DATABASE_URL: str = "postgresql://postgres:admin@postgres_db:5432/mydatabase"

    class Config:   # Esta clase se utiliza para configurar el comportamiento de carga de variables de entorno.
        env_file = ".env"  # Si existe un archivo .env, sus valores sobrescribirán los valores por defecto definidos arriba.
        env_file_encoding = "utf-8" # Especifica la codificación del archivo .env (en este caso, UTF-8).
        

auth_config = AuthConfig()