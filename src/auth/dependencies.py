from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from src.auth.utils import decode_token
from src.database import SessionLocal
# Configura OAuth2PasswordBearer para usar la ruta de login como URL de obtención de tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Función para obtener el usuario actual autenticado
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
        # Decodifica el token JWT
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise credentials_exception
    
    db = SessionLocal()
    try:# Busca al usuario en la base de datos usando el email (campo "sub" del token)
        user = get_user_by_email(payload["sub"])
        if user is None:
            raise credentials_exception
        return user
    finally:
        db.close()