from pydantic import BaseModel
from deck.deck import Deck 

class BJState(BaseModel):
    players: list[str]
    hands:   dict[str, Deck] 

class Blackjack:

    def __init__(self):
        ...

    def bet(self, player: int, bet_amount: int):
        ...

    def deal_card(self, player: int):
        ...



if __name__ == "__main__":
    
    # Instance of blackjack game created  
    game = Blackjack()

    # Create a new deck

    while players:
    # While there are players at the table
       
        # go around all players in game and give them their first card
        for player in players:

            game.deal_card(player)


        # Give dealer his card

        

    ...
