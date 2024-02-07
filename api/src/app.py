from datetime import date
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import *

import deck

app = FastAPI()

# TODO: LOOK MORE INTO THESE LATER
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"Hello": "World"}


class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    """
    This endpoint is used to create a new user account.

    It takes in a POST request containing the form data 
    from the sign up page.

    It sends HTTP 200 response if an account was properly
    created and ___ on error.
    """
    print(user) 

    return user 
    #return {"Status": "Created account succesfully"}


@app.get("/signin")
def signin():
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

      
    """
    pass

@app.post("/user")
def get_user():
    """
    This endpoint is used to get information of 
    currently authenticated user.

    It takes in the user id and returns a json
    response containing the respective user's 
    data.
    """
    pass
