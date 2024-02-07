from datetime import date
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, create_model
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session


class UserAuth(BaseModel):
    username: str
    password: str


class User(SQLModel, table=True):
# class User(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    dob: date 
    credits: Optional[int] = Field(default=0)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

engine = create_engine(sqlite_url, echo=True)

app = FastAPI()

# TODO: LOOK MORE INTO THESE LATER
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
def on_startup():
    create_db_and_tables()

@app.get("/")
def index():
    return {"Hello": "World"}


@app.post("/register")
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

    print("TYPE: ", type(user.dob))

    dob_str = str(user.dob)

    user.dob = date(*list(map(int, dob_str.split('-'))))

    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        print(user.id)
        return user


    # Hash password

    # Create id for new user (from database)

    # Save data in db (Potentially use SQLModel)
    return {"Status": user.id}


@app.get("/signin")
def signin(auth_pair: UserAuth):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

   
    """

    
    

    pass

@app.get("/user/{user_id}")
def get_user(user_id: int):
    """
    This endpoint is used to get information of 
    currently authenticated user.

    It takes in the user id and returns a json
    response containing the respective user's 
    data.
    """
    return {"response": user_id}
    pass
