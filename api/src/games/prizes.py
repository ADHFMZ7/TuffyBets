import random
from enum import Enum

class PrizeType(Enum):
    COINS = "coins"
    VANITY = "vanity"

class Prize:
    def __init__(self, name: str, value: int, prize_type: PrizeType):
        self.name = name
        self.value = value
        self.prize_type = prize_type

    def __str__(self):
        return f"{self.name}: {self.value} {self.prize_type}"

class PrizePool:
    def __init__(self):
        self.prizes = [
            Prize("50 Coins", 50, PrizeType.COINS),
            Prize("100 Coins", 100, PrizeType.COINS),
            Prize("150 Coins", 150, PrizeType.COINS),
            Prize("200 Coins", 200, PrizeType.COINS),
            Prize("250 Coins", 250, PrizeType.COINS),
            Prize("300 Coins", 300, PrizeType.COINS),
            Prize("350 Coins", 350, PrizeType.COINS),
            Prize("400 Coins", 400, PrizeType.COINS),
            Prize("450 Coins", 450, PrizeType.COINS),
            Prize("500 Coins", 500, PrizeType.COINS),
            Prize("Golden Crown", 1000, PrizeType.VANITY),
            Prize("Diamond Ring", 1500, PrizeType.VANITY),
            Prize("Platinum Watch", 2000, PrizeType.VANITY),
            Prize("Crystal Chandelier", 2500, PrizeType.VANITY),
            Prize("Luxury Yacht", 3000, PrizeType.VANITY),
            Prize("Mansion", 3500, PrizeType.VANITY),
            Prize("Private Island", 4000, PrizeType.VANITY),
            Prize("Space Travel Ticket", 4500, PrizeType.VANITY),
            Prize("Time Machine", 5000, PrizeType.VANITY),
            Prize("Eternal Happiness", 10000, PrizeType.VANITY)
        ]

    def add_prize(self, name: str, value: int, prize_type: PrizeType):
        """
        Adds a customizable prize

        Parameters
        name - name of prize
        value - monetary value of prize 
        prize_type - vanity or coins

        """

        new_prize = Prize(name, value, prize_type)
        self.prizes.append(new_prize)

        return 0
    
    def get_prize_by_name(self, name: str) -> Prize:

        """
        Returns the prize by name from the prize pool

        Parameters
        name - name of prize

        """

        for prize in self.prizes:
            if prize[0] == name:
                return prize
        return None
    
    def get_random_prize(self, seed: int = 0) -> Prize:

        """
        Chooses a random prize directly coorelated with the values, the odds
        are inversely related with the value

        Parameters
        seed - used for randomizing random.choice
        """

        if seed: random.seed(seed)

        weighted_choices = [(prize, 1 / prize.value) for prize in self.prizes]
        prizes, weights = zip(*weighted_choices)
        chosen_prize = random.choices(prizes, weights=weights)[0]

        return chosen_prize
