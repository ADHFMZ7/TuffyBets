from fastapi import APIRouter, Depends
from typing import Annotated
from models import User
from dependencies import oauth2_scheme, get_current_user
# from models import GameUpdate
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
