from fastapi import APIRouter
from datetime import date
from models import User, UserAuth


router = APIRouter()


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

    print("TYPE: ", type(user.dob))

    dob_str = str(user.dob)

    user.dob = date(*list(map(int, dob_str.split('-'))))

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
    return {"Status": user.id}


@router.get("/signin")
def signin(auth_pair: UserAuth):
    """
    This endpoint is used to authenticate a user to 
    gain access to their existing account.

   
    """
    pass
