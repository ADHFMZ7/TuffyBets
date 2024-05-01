from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from dependencies import oauth2_scheme, get_current_user, get_session
from models import UserBase, UserUpdate, User
from sqlmodel import Session
from db import update_user, get_transactions_query, get_user_by_id
from pydantic import BaseModel
from datetime import date
# from ..games.roulette import Roulette
import random 
from typing import Dict

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
    
    if prev_spin := get_transactions_query(session, date.today(), user.id, "Daily Spin"):
        print("User already spun the wheel today")
        print("Previous spin: ", prev_spin[0].amount)
        options = [int(random.expovariate(1/1000)) for _ in range(15)]
        options[0] = prev_spin[0].amount
        win_index = 0
    else: 
        options = [int(random.expovariate(1/1000)) for _ in range(15)] 
        win_index = random.choice(range(len(options)))
        update_user(session, user.id, UserUpdate(credits=options[win_index]), "Daily Spin")
        
   
    print(f"User {user.username} won {options[win_index]} credits")
    
    return {
        "win_index": win_index,
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



class BetData(BaseModel):
    icon: str
    number: int

class BetRoulette(BaseModel):
    bets: Dict[str, BetData]

@router.post("/roulette")
def bet_roulette(data: BetRoulette, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    # Define payout rates for different bet types
    payouts = {
        "straight": 36,  # Bet on a single number
        "dozen": 3,      # Bet on a dozen (1st, 2nd, or 3rd)
        "column": 3,     # Bet on a column (1st, 2nd, or 3rd)
        "even_odd": 2,   # Bet on even or odd
        "low_high": 2,   # Bet on low (1-18) or high (19-36)
        "color": 2,      # Bet on red or black
        "street": 12,    # Bet on a street (3 numbers)
        "split": 18,     # Bet on a split (2 numbers)
        "corner": 9,     # Bet on a corner (4 numbers)
        "six_line": 6    # Bet on a six line (6 numbers)
    }
 
    data = data.bets
  
    total_bet = sum([bet_data.number for bet_data in data.values()])
    total_winnings = 0


    userdb = get_user_by_id(session, user.id)
    print(userdb) 
   
    if total_bet > userdb.credits:
        raise HTTPException(status_code=400, detail="Insufficient funds")
  
    total_winnings -= total_bet
   
    winning_number = random.randint(0, 37)
    
    
    for bet_type, bet_data in data.items():

            number = bet_data.number
           
            
            if bet_type == "00":
                if winning_number == 37:
                    total_winnings += payouts["straight"] * number
            
            elif bet_type.isdigit(): # STRIGHT
                print("STRIGN")
                if int(bet_type) == winning_number:
                    total_winnings += payouts["straight"] * number
                
            elif "1ST_DOZEN" == bet_type:
                if winning_number in range(1, 13):
                    total_winnings += payouts["dozen"] * number
            elif "2ND_DOZEN" == bet_type:
                if winning_number in range(13, 25):
                    total_winnings += payouts["dozen"] * number
            elif "3RD_DOZEN" == bet_type:
                if winning_number in range(25, 37):
                    total_winnings += payouts["dozen"] * number
             
            elif bet_type == "RED":
                if winning_number in [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]:
                    total_winnings += payouts["color"] * number
                
            elif bet_type == "BLACK":
                if winning_number in [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]:
                    total_winnings += payouts["color"] * number
               
            elif bet_type == "EVEN":
                if winning_number != 0 and winning_number % 2 == 0:
                    total_winnings += payouts["even_odd"] * number
            
            elif bet_type == "ODD":
                if winning_number != 0 and winning_number % 2 == 1:
                    total_winnings += payouts["even_odd"] * number
            
            elif bet_type == "1_TO_18":
                if winning_number in range(1, 19):
                    total_winnings += payouts["low_high"] * number
                    
            elif bet_type == "19_TO_36":
                if winning_number in range(19, 37):
                    total_winnings += payouts["low_high"] * number
                
           
            else:
                # Unknown bet type, raise an exception
                raise HTTPException(status_code=400, detail=f"Unknown bet type: {bet_type}")
          
    update_user(session, user.id, UserUpdate(credits=total_winnings), "Roulette")
        
    return {"winning_number": winning_number, "winnings": total_winnings}
