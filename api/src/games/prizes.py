import random

class Prize:
    def __init__(self):
        self.prizes = [
            ("50 Coins", 50, "coins"),
            ("100 Coins", 100, "coins"),
            ("150 Coins", 150, "coins"),
            ("200 Coins", 200, "coins"),
            ("250 Coins", 250, "coins"),
            ("300 Coins", 300, "coins"),
            ("350 Coins", 350, "coins"),
            ("400 Coins", 400, "coins"),
            ("450 Coins", 450, "coins"),
            ("500 Coins", 500, "coins"),
            ("Golden Crown", 1000, "vanity"),
            ("Diamond Ring", 1500, "vanity"),
            ("Platinum Watch", 2000, "vanity"),
            ("Crystal Chandelier", 2500, "vanity"),
            ("Luxury Yacht", 3000, "vanity"),
            ("Mansion", 3500, "vanity"),
            ("Private Island", 4000, "vanity"),
            ("Space Travel Ticket", 4500, "vanity"),
            ("Time Machine", 5000, "vanity"),
            ("Eternal Happiness", 10000, "vanity")
        ]

    def add_prize(self, name: str, value: int, prize_type: str):
        """
        Adds a customizable prize

        Parameters
        name - name of prize
        value - monetary value of prize 
        prize_type - vanity or coins

        """

        new_prize = (name, value, prize_type)
        self.prizes.append(new_prize)

        return 0
    
    def get_prize_by_name(self, name: str) -> tuple[str, int, str]:

        """
        Returns the prize by name from the prize pool

        Parameters
        name - name of prize

        """

        for prize in self.prizes:
            if prize[0] == name:
                return prize
        return None
    
    def get_random_prize(self, seed: int = 0) -> tuple[str, int, str]:

        """
        Chooses a random prize directly coorelated with the values, the odds
        are inversely related with the value

        Parameters
        seed - used for randomizing random.choice
        """

        if seed: random.seed(seed)

        weighted_choices = [(prize, 1 / prize[1]) for prize in self.prizes]
        prizes, weights = zip(*weighted_choices)
        chosen_prize = random.choices(prizes, weights=weights)[0]

        return chosen_prize
