import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.auth.schemas import Token, UserCreate, UserResponse
from src.auth.service import authenticate_user, create_user
from src.auth.utils import create_access_token
from src.auth.config import auth_config
from src.models import User
from src.auth.dependencies import get_current_user

router = APIRouter(tags=["Authentication"])
logger = logging.getLogger(__name__)


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            logger.warning(f"Usuario {form_data.username} no autenticado")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario o contraseña incorrectos",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
        access_token_expires = timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, 
            expires_delta=access_token_expires
        )
    
        logger.info(f"Login exitoso para: {user.email}")
        return {"access_token": access_token, "token_type": "bearer"}
    
    except Exception as e:
        logger.error(f"Error en login: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error en login"
        )

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    try:
        new_user = create_user(user_data)
        logger.info(f"Usuario registrado: {new_user.email}")
        return new_user
        
    except ValueError as e:
        logger.error(f"Error en registro: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str("Error interno del servidor")
        )
    except Exception as e:
        logger.error(f"Error inesperado en registro: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )
        
@router.post("cvs/", tags=["CVs"])
async def create_cv(cv_data: dict, user: User = Depends(get_current_user)):
    return {"message": "Cv created", "user_id": user.id}
