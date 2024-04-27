from fastapi import APIRouter, Depends
from typing import Annotated
from dependencies import oauth2_scheme, get_current_user, get_session
from models import UserBase, UserUpdate, User
from sqlmodel import Session
from db import update_user
from pydantic import BaseModel
# from ..games.roulette import Roulette
import random 

router = APIRouter()

# @router.get("/{game_id}")
# def join_game(game_id: int):
#     pass

# @router.post("/{game_id}")
# def take_action(game_id: int, action: GameUpdate):
#     pass

@router.get("/daily-spin")
def spin_wheel(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    """
    Randomly chooses from prize pool

    """
    # TODO: check if user has done daily spin yet
    
    options = [int(random.expovariate(1/1000)) for _ in range(15)] 
    rand_credits = random.choice(range(len(options)))
    
    update_user(session, user.id, UserUpdate(credits=user.credits + rand_credits))

    return {
        "credits": rand_credits,
        "options": options
    }

@router.get("/daily-login")
def login_bonus(user: User = Depends(get_current_user), session: Session = Depends(get_session)) -> int:
    """
    Adds 1000 credits to user's account

    """
    user.credits += 1000

    update_user(session, user.id, UserUpdate(credits=user.credits))
    return 1000


###### 

class Roulette_Bet(BaseModel):
    color: str = None
    number: int = None 
    bet_amount: int


@router.post("/roulette")
def bet_roulette(bets: Roulette_Bet, user: User = Depends(get_current_user), session: Session = Depends(get_session)) -> int:
    """
    Bet on a color in roulette

    """
    bet_amount = bets.bet_amount
    if user.credits < bet_amount:
        return {"error": "Insufficient funds"}

    user.credits -= bet_amount

    update_user(session, user.id, UserUpdate(credits=user.credits))

    # roulette_game = Roulette(time.time())
    # winnings, spun_number, spun_color = roulette_game.bet_color(color, bet_amount)

    # user.credits += winnings

    # update_user(session, user.id, UserUpdate(credits=user.credits))

    # return winnings