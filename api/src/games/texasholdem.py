from pydantic import BaseModel
from deck.deck import Deck
from enum import Enum

class PKState(BaseModel):
    players: list[int]
    hands:   dict[str, Deck]

class PlayerID(Enum):
	BIGBLIND = 1
	UNDERTHEGUN = 2
	LOJACK = 3
	HIJACK = 4
	CUTOFF = 5
	BUTTON = 6
	SMALLBLIND = 7

class TexasHoldem:

	def __init__(self):
		gameState = 1
		money_pot = 0
		isPreFlop = True
		deck = Deck(1)
		deck.shuffle()

	def bet(self, player: int, bet_amount: int):
		if player == 1 or player == 7:
			money_pot += bet_amount
		else:
			return

	def controlled_bet(self, player:int, bet_amount: int):
		money_pot += bet_amount

	def raise_bet(self, player:int, bet_amount: int):
		money_pot += 2*bet_amount

    def deal_card(self, player: int):
    	deck.draw(deck, 1, " ")

if __name__ == "__main__":
    
    game = TexasHoldem()

    # Create a new deck

    current_bet = 1
    bet_option = 0
    raise_bet_option = 0
    current_player = 1
    number_of_players = 1
    player_financial_account = 0
    player_won = False

    while players:
    # While there are players at the table
       
        # go around all players in game and give them their first card
        for player in players:

        	for i in range(1, 8):
            	player = PlayerID(i).value

            game.deal_card(player)

        game.bet(current_player, current_bet)

        if(current_bet <= 0):
        	print("Unable to play game at the moment. Bet must be greater than zero.")

        current_player++

        for current_player in range(2, 8):
        	if bet_option == 1:
        		game.controlled_bet(current_player, current_bet)
        	elif bet_option == 2:
        		game.raise_bet(current_player, current_bet)
        		for i in range(1, current_player):
        			if raise_bet_option == 1:
        				game.raise_bet(i, current_bet)
        			else:
        				players.remove(PlayerID(i).value)
        		for j in range(current_player+1, 8):
        			if raise_bet_option == 1:
        				game.raise_bet(j, current_bet)
        			else:
        				players.remove(PlayerID(j).value)
        	else:
        		players.remove(PlayerID(current_player).value)

        game.gameState++

        if game.gameState != 1:
			game.isPreFlop = False

		for number_of_players in range(1, 8):
			number_of_players += players.count(PlayerID(number_of_players).value)

		if number_of_players > 1:

			if game.gameState == 2:

				game.deck.draw(game.deck, 1, " ")

				for i in range(1, 4):
					game.deck.draw(game.deck, i, " ")

				if players.count(PlayerID(7).value) != 0:
					if bet_option == 1:
						game.bet(7, current_bet)
					elif bet_option == 3:
						game.bet(7, 0)

				for k in range(1, 7):
					if players.count(PlayerID(k).value != 0):
						if bet_option == 1:
        					game.controlled_bet(k, current_bet)
        				elif bet_option == 2:
        					game.raise_bet(k, current_bet)
        					for i in range(1, k):
        						if raise_bet_option == 1:
        							game.raise_bet(i, current_bet)
        						else:
        							players.remove(PlayerID(i).value)
        							number_of_players--
        					for j in range(k+1, 7):
        						if raise_bet_option == 1:
        							game.raise_bet(j, current_bet)
        						else:
        							players.remove(PlayerID(j).value)
        							number_of_players--
        				else:
        					players.remove(PlayerID(k).value)
        					number_of_players--
        		game.gameState++

		else:
			return

		while number_of_players > 1:
			if game.gameState == 3:

				for i in range(1, 3):
					game.deck.draw(game.deck, i, " ")

				if players.count(PlayerID(7).value) != 0:
					if bet_option == 1:
						game.bet(7, current_bet)
					elif bet_option == 3:
						game.bet(7, 0)

				for k in range(1, 7):
					if players.count(PlayerID(k).value) != 0:
						if bet_option == 1:
        					game.controlled_bet(k, current_bet)
        				elif bet_option == 2:
        					game.raise_bet(k, current_bet)
        					for i in range(1, k):
        						if raise_bet_option == 1:
        							game.raise_bet(i, current_bet)
        						else:
        							players.remove(PlayerID(i).value)
        							number_of_players--
        					for j in range(k+1, 7):
        						if raise_bet_option == 1:
        							game.raise_bet(j, current_bet)
        						else:
        							players.remove(PlayerID(j).value)
        							number_of_players--
        				else:
        					players.remove(PlayerID(k).value)
        					number_of_players--
			elif game.gameState == 4:

				for i in range(1, 3):
					game.deck.draw(game.deck, i, " ")

				if players.count(PlayerID(7).value) != 0:
					if bet_option == 1:
						game.bet(7, current_bet)
					elif bet_option == 3:
						game.bet(7, 0)

				for k in range(1, 7):
					if players.count(PlayerID(k).value) != 0:
						if bet_option == 1:
        					game.controlled_bet(k, current_bet)
        				elif bet_option == 2:
        					game.raise_bet(k, current_bet)
        					for i in range(1, k):
        						if raise_bet_option == 1:
        							game.raise_bet(i, current_bet)
        						else:
        							players.remove(PlayerID(i).value)
        							number_of_players--
        					for j in range(k+1, 7):
        						if raise_bet_option == 1:
        							game.raise_bet(j, current_bet)
        						else:
        							players.remove(PlayerID(j).value)
        							number_of_players--
        				else:
        					players.remove(PlayerID(k).value)
        					number_of_players--

        	elif game.gameState == 5:

				for k in range(1, 7):
					if players.count(PlayerID(k).value) != 0:
						for card in game.deck._cards:
							if card > game.deck._cards.rank or card > game.deck._cards.suit:
								player_won = True

				if(player_won == True):
					player_financial_account += game.money_pot;
