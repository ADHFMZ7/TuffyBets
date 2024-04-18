from pydantic import BaseModel
from deck.deck import Deck
from enum import Enum

import random
import time

class PKState(BaseModel):
	gameState: int
    players: list[str]
    hands:   dict[str, Deck]

class PlayerID(Enum):
	SMALLBLIND = 1
	BIGBLIND = 2
	UNDERTHEGUN = 3
	LOJACK = 4
	HIJACK = 5
	CUTOFF = 6
	BUTTON = 7

class TexasHoldem:

	def __init__(self):
		money_pot = 0
		isPreFlop = False
		deck = Deck()
		deck.shuffle()

	def bet(self, player: int, bet_amount: int):
		if player == PlayerID.UNDERTHEGUN.value:
			isPreFlop = True
		else:
			isPreFlop = False

		if player == 1 or player == 3:
			money_pot += bet_amount
		else:
			return

    def deal_card(self, player: int):
    	deck.draw(deck, 1, " ")

if __name__ == "__main__":
    
    game = TexasHoldem()

    # Create a new deck

    while players:
    # While there are players at the table
       
        # go around all players in game and give them their first card
        for player in players:

        	for i in range(7):
            	player = PlayerID(i).name

            game.deal_card(player)

        game.bet(3, 2)

        
