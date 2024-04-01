from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer    
from models import User
from typing import Annotated
from db import engine, get_user_by_id
from sqlmodel import Session
from jose import jwt, JWTError
from security import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    """
    Fetches data from the currently 
    authenticated user.
    
    Parameters:
        token: The bearer auth token 
        
    Returns: 
        User: The user that created the provided token 
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD: ", payload)
        id = payload.get("id")
        if not id:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    with Session(engine) as session:
        user = get_user_by_id(session, id)
        
    if not user:
        raise credentials_exception
    
    return user

def get_session():
    with Session(engine) as session:
        yield session
