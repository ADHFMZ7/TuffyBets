from fastapi import APIRouter, Depends
from typing import Annotated
from dependencies import oauth2_scheme, get_current_user, get_session
from models import UserBase, UserUpdate, User
from sqlmodel import Session
from db import update_user
import random 

router = APIRouter()

# @router.get("/{game_id}")
# def join_game(game_id: int):
#     pass

# @router.post("/{game_id}")
# def take_action(game_id: int, action: GameUpdate):
#     pass

@router.get("/daily-spin")
def spin_wheel(user: User = Depends(get_current_user)) -> int:
    """
    Randomly chooses from prize pool

    """
    rand_credits = int(random.gauss(1000, 100))
    user.credits += rand_credits

    return rand_credits

@router.get("/daily-login")
def login_bonus(user: User = Depends(get_current_user), session: Session = Depends(get_session)) -> int:
    """
    Adds 1000 credits to user's account

    """
    user.credits += 1000

    update_user(session, user.id, UserUpdate(credits=user.credits))
    return 1000