from enum import Enum
import time
import random
import json

class Suit(Enum):
    Hearts, Diamonds, Spades, Clubs = range(1, 5)
    
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
        return f"{str(self.rank.value).zfill(2)}{str(self.suit.value)}"

    def __str__(self):
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
        self.deck_count = deck_count

        self.add_hand("shoe")

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

        cards = []
        if hand_name == "shoe":
            cards = [Card(rank, suit)   for suit in Suit 
                                        for rank in Rank 
                                        for _ in range(self.deck_count)]
           
        self.hands[hand_name] = cards 

    def shuffle(self, hand: str = "shoe"):
        """
        Shuffles the deck of cards to a randomized configuration.

        Parameters:
            hand - The name of the hand to shuffle
        """

        if not self.hand_exists(hand):
            return False

        random.shuffle(self.hands[hand])

    def draw(self, num_cards: int, hand: str):
        """
        Draws cards from the top of the deck.

        parameters:
            num_cards - the number of cards to draw
            hand - the hand to deal the card to
        """

        self.hand_exists(hand) # Handle error

        for _ in range(num_cards):
            self.hands[hand].append(self.hands["shoe"].pop())


    def verify_deck(self):
        """
        Verifies that deck still contains all cards.

        """
        ... 

    def hand_exists(self, hand: str):
        """
        Verifies the hand name provided is a valid hand in the deck.

        parameters:
            hand: The name of the hand to be verified
        """
        return hand in self.hands.keys()

    def serialize(self):
        """
        Serializes the state of a deck of cards
        """
        hands = {}

        for hand in self.hands:
            hands[hand] = [repr(card) for card in self.hands[hand]]
        
        return {
            "deck_count": self.deck_count,
            "hands": hands,
        }

def verify_deck_json(deck):
    return True

def deserialize_deck(deck):
    
    if not verify_deck_json(deck):
        return False

    deck_count = deck["deck_count"]

    new_deck = Deck(deck_count)

    hands = deck["hands"].keys()
    for hand in hands:
        new_deck.hands[hand] = [Card(Rank(int(card_repr[:2])), Suit(int(card_repr[2]))) for card_repr in deck["hands"][hand]]

    return new_deck

if __name__ == "__main__":
    deck = Deck(1, seed=100)

    deck.add_hand("dealer")
    deck.add_hand("p1")
    deck.add_hand("p2")
    deck.add_hand("p3")

    for hand in deck.hands:
        deck.draw(2, hand)

    # for card in deck._cards:
    #     print(card)
    js = deck.serialize()

    # print(js)

    # print(json.dumps(
    #     js,
    #     indent=2,
    #     separators=(',', ': ')
    # ))

 
    for i in deck.hands["shoe"]:
        print(i)
    
    print(deserialize_deck(js).serialize() == js)

