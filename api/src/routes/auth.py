from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import date
from models import User, Token, UserReg, UserInDB
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

    if user_exists(session, user_reg.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    dob_str = str(user_reg.dob)

    hashed_pass = hash_password(user_reg.password)
    user_reg.dob = date(*list(map(int, dob_str.split('-'))))

    params = user_reg.model_dump()
    del params["password"]

    user = UserInDB(**params, hashed_password=hashed_pass)
    create_user(session, user)

    return {"user_id": user.id}


@router.post("/login")
# def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
def signin(form_data: OAuth2PasswordRequestForm = Depends(), session: Session=Depends(get_session)):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

    """
    user = validate_user(session, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt(data=user.model_dump(), expires_delta=access_token_expires)

    return Token(access_token=access_token, token_type="bearer")
