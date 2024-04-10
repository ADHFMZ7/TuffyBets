from pydantic import BaseModel
from deck.deck import Deck

import random
import time

class PKState(BaseModel):
    players: list[str]
    hands:   dict[str, Deck] 

class TexasHoldem:

	def __init__(self):
		BigBlind = 1
		SmallBlind = 2
		Button = 3
		CutOff = 4
		HiJack = 5
		LoJack = 6
		UnderTheGun = 7
		money_pot = 0
		isPreFold = False
		deck = Deck()
		deck.shuffle()

	def bet(self, player: int, bet_amount: int):
		if player == UnderTheGun:
			isPreFold = True
		else:
			isPreFold = False

		if player == 2 or player == 7:
			money_pot += bet_amount
		else:
			return

    def deal_card(self, player: int):
    	if player == 2 or player == 7:
    		deck.draw(deck, 1, " ")

if __name__ == "__main__":
    
    game = TexasHoldem()

    # Create a new deck

    while players:
    # While there are players at the table
       
        # go around all players in game and give them their first card
        for player in players:

            game.deal_card(player)

