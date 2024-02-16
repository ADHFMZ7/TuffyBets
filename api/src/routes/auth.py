from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import date
from models import User, Token


router = APIRouter()

temp_db = {
    "user1": User(username="user1", password="pass", dob=date(2024, 2, 16))
}

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

    # TEMP DB CODE BELOW THIS ###########
    if user.username in temp_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    temp_db[user.username] = user
    # TEMP DB CODE ABOVE THIS ########


    # Hash password

    # Create id for new user (from database)

    # Save data in db (Potentially use SQLModel)
    return {"ID": user.id}


@router.post("/signin", response_model=Token)
# def signin(username: Annotated[str, Form()], password: Annotated[str, Form()]):
def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

    """
    user = temp_db.get(form_data.username)
    print(user)

    if not user or form_data.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
    return {"access_token": access_token, "token_type": "bearer"}
