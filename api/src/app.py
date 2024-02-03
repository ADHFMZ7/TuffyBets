from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.post("/register")
def register():
    """
    This endpoint is used to create a new user account.

    It takes in a POST request containing the form data 
    from the sign up page.

    It sends HTTP 200 response if an account was properly
    created and ___ on error.
    """
    pass

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





