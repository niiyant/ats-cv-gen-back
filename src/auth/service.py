from passlib.context import CryptContext 
# Importa CryptContext de passlib para manejar el hashing de contraseñas
from src.database import SessionLocal      
from src.models import User
from src.auth.schemas import UserCreate

# Crea una instancia de CryptContext para usar bcrypt como esquema de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para obtener un usuario por su email
def get_user_by_email(email: str):
    db = SessionLocal()
    try: # Busca el primer usuario en la base de datos que coincida con el email proporcionado
        user = db.query(User).filter(User.email == email).first()
        return user
    finally:
        db.close() # Cierra la sesión de la base de datos para liberar recursos

# Función para autenticar un usuario
def authenticate_user(email: str, password: str):
    user = get_user_by_email(email) # Verifica si el usuario existe y si la contraseña es correcta
    if not user or not verify_password(password, user.password_hash):
        return False
    return user

# Función para crear un nuevo usuario
def create_user(user_data: UserCreate):
    db = SessionLocal()
    try:    # Verifica si ya existe un usuario con el mismo email
        if get_user_by_email(user_data.email):
            raise ValueError("Email already registered")
        # Hashea la contraseña proporcionada usando bcrypt
        hashed_password = pwd_context.hash(user_data.password)
        
         # Crea una nueva instancia del modelo User con los datos proporcionados
        db_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
        # Añade el nuevo usuario a la sesión de la base de datos
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db.close()
        return db_user
    finally:    # Asegura que la sesión de la base de datos se cierre incluso si hay un error
        db.close()