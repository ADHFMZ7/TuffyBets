from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import date, timedelta
from models import User, Token, UserReg
from db import get_user_by_id, user_exists, create_user, get_user_by_username
from dependencies import get_session
from sqlmodel import Session
from security import validate_user, hash_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_jwt

router = APIRouter()


@router.post("/register")
def register(user_reg: UserReg, session: Session = Depends(get_session)):
    """
    This endpoint is used to create a new user account.

    It takes in a POST request containing the form data 
    from the sign up page.

    It sends HTTP 200 response if an account was properly
    created and ___ on error.
    """
    
    if user_reg.dob > date.today() or user_reg.dob < date(1900, 1, 1):
        raise HTTPException(status_code=400, detail="Invalid date of birth") 
    
    if date.today().year - user_reg.dob.year < 21:
        raise HTTPException(status_code=400, detail="You must be at least 21 years old to register")

    if user_exists(session, user_reg.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    dob_str = str(user_reg.dob)

    hashed_pass = hash_password(user_reg.password)
    user_reg.dob = date(*list(map(int, dob_str.split('-'))))

    params = user_reg.model_dump()
    del params["password"]
    user_reg.id = None

    user = User(**params, hashed_password=hashed_pass)
    create_user(session, user)

    return {"user_id": user.id}


@router.post("/login")
def signin(form_data: OAuth2PasswordRequestForm = Depends(), session: Session=Depends(get_session)):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

    """
    user = validate_user(session, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    user_data = user.model_dump()
    del user_data["hashed_password"]
    user_data["dob"] = str(user_data["dob"])

    access_token = create_jwt(data=user_data, expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type="bearer")
