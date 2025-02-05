from datetime import datetime, timedelta
from jose import jwt # Importa la librería JOSE para trabajar con tokens JWT
from src.auth.config import auth_config

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Crea un token JWT de acceso.
    
    Args:
        data (dict): Datos a incluir en el token (normalmente el email del usuario)
        expires_delta (timedelta | None): Tiempo de expiración del token
        
    Returns:
        str: Token JWT firmado
    """
    to_encode = data.copy() # Crea una copia de los datos para no modificar el original
    
    # Configurar tiempo de expiración
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    # Añadir claim de expiración
    to_encode.update({"exp": expire}) # Agrega la fecha de expiración al payload del token
    
    # Generar el token JWT
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=auth_config.SECRET_KEY,
        algorithm=auth_config.ALGORITHM
    )
    
    return encoded_jwt  # Devuelve el token JWT generado

def decode_token(token: str) -> dict | None:
    try:     # Intenta decodificar el token JWT
        payload = jwt.decode(
            token=token,    # Token JWT a decodificar
            key=auth_config.SECRET_KEY,  # Clave secreta para verificar la firma
            algorithms=[auth_config.ALGORITHM]
        )
        return payload  # Devuelve el payload decodificado si es válido
    except jwt.JWTError as e:
        print(f"Error decodificando token: {e}")
        return None