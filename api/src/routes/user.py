from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from dependencies import oauth2_scheme, get_session
from db import get_user_by_id
from models import UserBase
from sqlmodel import Session

router = APIRouter()

@router.get("/{user_id}")
def get_user(user_id: int, token: Annotated[str, Depends(oauth2_scheme)], session: Session = Depends(get_session)):
    """
    This endpoint is used to get information of 
    currently authenticated user.

    It takes in user id and returns a json
    response containing the respective user's 
    data.
    """
    user = get_user_by_id(session, user_id)

    if not user:
        raise HTTPException(status_code=400, detail="User ID does not exist")

    user_data = user.model_dump()

    del user_data["hashed_password"]

    return UserBase(**user_data)
