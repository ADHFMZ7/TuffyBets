from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from dependencies import oauth2_scheme, get_session, get_current_user
from db import get_user_by_id, store_transaction
from models import UserBase, Transaction, User
from sqlmodel import Session, select
from datetime import date
from jose import jwt, JWTError
from security import SECRET_KEY, ALGORITHM

router = APIRouter()



@router.post("/transactions")
def create_transaction(transaction: Transaction, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    """
    This endpoint is used to create a new transaction
    made by a user.

    It takes in user id and returns a json response
    containing the respective user's data.
    """
    print("USER: ", user)
    transaction.user_id = int(user.id)

    transaction.date = date(*list(map(int, transaction.date.split('-'))))

    store_transaction(session, transaction)

    print("TRANSACTION: ", transaction)
    return transaction

@router.get("/transactions")
def get_transactions(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    """
    This endpoint is used to get all transactions
    made by a user.

    It takes in user id and returns a list of 
    transactions made by the respective user.
    """
    if not user:
        raise HTTPException(status_code=400, detail="User ID does not exist")

    transactions = session.exec(select(Transaction).where(Transaction.user_id == user.id)).all()

    return transactions


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