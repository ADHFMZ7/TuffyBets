from fastapi import APIRouter, Depends
from typing import Annotated
from dependencies import oauth2_scheme

router = APIRouter()

@router.get("/")
def get_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    This endpoint is used to get information of 
    currently authenticated user.

    It takes in the auth token and returns a json
    response containing the respective user's 
    data.
    """
    return {"token": token}
    return {"response": user_id}


