from enum import Enum
import time
import random

class Suit(Enum):
    hearts, diamonds, spades, clubs = range(1, 5)
    
    def __str__(self): return self.name

class Rank(Enum):
    Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten = range(2, 11)
    Jack, Queen, King, Ace = range(11, 15)

    def __str__(self): return self.name

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank  = rank 
        self.suit  = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self, deck_count: int = 1, seed: int = 0):
        """
        Initializes a Deck object

        The Deck object 

        parameters:
            deck_count: the number of decks to be added. defaults to one.
            seed: sets seed for the random number generator to be used.
        """        

        self.hands = {}
        self._cards = [Card(rank, suit) for suit in Suit 
                                        for rank in Rank 
                                        for _ in range(deck_count)]

        self.seed = seed if seed else int(time.time())
        random.seed(self.seed)
        self.shuffle()

    def add_hand(self, hand_name: str):
        """
        Creates a new hand to be used in games.

        Each hand contains a list of cards.

        Parameters:
            hand_name - The name of the hand to be created.
        """

        self.hands[hand_name] = []

    def shuffle(self, hand: str = ""):
        """
        Shuffles the deck of cards to a randomized configuration.

        Parameters:
            hand - The name of the hand to shuffle
        """

        if hand: self.verify_hand(hand)

        random.shuffle(self._cards) if not hand else random.shuffle(self.hands[hand])

    def draw(self, num_cards: int, hand):
        """
        Draws cards from the top of the deck.

        parameters:
            num_cards - the number of cards to draw
        """

        self.verify_hand(hand) # Handle error

        for _ in range(num_cards):
            self.hands[hand].append(self._cards.pop())


    def verify_deck(self):
        """
        Verifies that deck still contains all cards.

        """
        ... 

    def verify_hand(self, hand: str):
        """
        Verifies the hand name provided is a valid hand in the deck.

        parameters:
            hand: The name of the hand to be verified
        """
        return hand in self.hands.keys()

if __name__ == "__main__":
    deck = Deck(1, seed=100)
    for card in deck._cards:
        print(card)

