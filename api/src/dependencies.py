from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer    
from models import User
from typing import Annotated
from db import engine
from sqlmodel import Session

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
    ...

def get_session():
    with Session(engine) as session:
        yield session
