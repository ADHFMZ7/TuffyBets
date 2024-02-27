from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import date
from models import User, Token
from db import get_user_by_id, user_exists, create_user, get_user_by_username
from dependencies import get_session
from sqlmodel import Session


router = APIRouter()


@router.post("/register")
def register(user: User, session: Session = Depends(get_session)):
    """
    This endpoint is used to create a new user account.

    It takes in a POST request containing the form data 
    from the sign up page.

    It sends HTTP 200 response if an account was properly
    created and ___ on error.
    """


    if user_exists(session, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    dob_str = str(user.dob)

    user.dob = date(*list(map(int, dob_str.split('-'))))

    # Hash password (IMPLEMENTED LATER)
    # TODO: hashed passwords

    user_id = create_user(session, user)

    if not user_id:
        raise HTTPException(status_code=400, detail="Failed to create user")

    return {"ID": user_id}


@router.post("/signin", response_model=Token)
# def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
def signin(form_data: OAuth2PasswordRequestForm = Depends(), session: Session=Depends(get_session)):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

    """
    user = get_user_by_username(session, form_data.username)

    if not user or form_data.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")


    # TODO: more secure tokens later
    return {"access_token": user.username, "token_type": "bearer"}
