from fastapi import APIRouter, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import date
from models import User, Token


router = APIRouter()

temp_db = {}

@router.post("/register")
def register(user: User):
    """
    This endpoint is used to create a new user account.

    It takes in a POST request containing the form data 
    from the sign up page.

    It sends HTTP 200 response if an account was properly
    created and ___ on error.
    """

    # Check if username exists
        # if it does, return user exists error

    dob_str = str(user.dob)

    user.dob = date(*list(map(int, dob_str.split('-'))))
    user.id = len(temp_db) + 1

    # TEMP DB CODE 
    temp_db[user.username] = user

    # with Session(engine) as session:
    #     session.add(user)
    #     session.commit()
    #     session.refresh(user)
    #     print(user.id)
    #     return user
    print(user)

    # Hash password

    # Create id for new user (from database)

    # Save data in db (Potentially use SQLModel)
    return {"ID": user.id}


# @router.post("/signin", response_model=Token)
@router.post("/signin")
# def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

   
    """

    
    # print("USERNAME:", username)
    # print("PASSWORD:", password)

    print("USERNAME:", form_data.username)
    print("PASSWORD:", form_data.password)
    pass
