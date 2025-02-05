from pydantic import BaseModel, EmailStr
from datetime import datetime

# Define un esquema para representar un token JWT
class Token(BaseModel):
    access_token: str # Contiene el token JWT de acceso
    token_type: str     # Especifica el tipo de token (por ejemplo, "bearer")

# Define un esquema base para un usuario
class UserBase(BaseModel):
    email: EmailStr

# Define un esquema para la creación de un usuario, heredando de UserBase
class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str

# Define un esquema para la respuesta de un usuario, heredando de UserBase
class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Permite la creación del esquema desde un objeto ORM (como SQLAlchemy)