from datetime import datetime, timedelta
from jose import jwt
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
    to_encode = data.copy()
    
    # Configurar tiempo de expiración
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    # Añadir claim de expiración
    to_encode.update({"exp": expire})
    
    # Generar el token JWT
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=auth_config.SECRET_KEY,
        algorithm=auth_config.ALGORITHM
    )
    
    return encoded_jwt

def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(
            token=token,
            key=auth_config.SECRET_KEY,
            algorithms=[auth_config.ALGORITHM]
        )
        return payload
    except jwt.JWTError as e:
        print(f"Error decodificando token: {e}")
        return None