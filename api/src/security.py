from sqlmodel import Session
from db import get_user_by_username
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from models import Token, User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" # TODO: Generate our own and take as env var later
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 9999

def hash_password(password: str) -> str:
    """
    generates hash corresponding to given password

    parameters:
        password: str - password to be hashed

    returns:
        str - password hashed with bcrypt hashing function
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def validate_user(session: Session, username: str, password: str) -> User | None:
    user = get_user_by_username(session, username)

    if not user:
        return None

    if verify_password(password, user.hashed_password):
        return user

    return None

def create_jwt(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

