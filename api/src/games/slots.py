import random
import time 


class Slots:

    def __init__(self, seed: int, symbols: dict[str, int]) -> None:
        """
        Initializes the slot machine.

        Sets the random seed and symbols 
        on the reel.

        parameters:
        seed - Sets the seed for the random number generation
        symbols -- The symbols and their point values
        """

        if seed: random.seed(seed)
        self.symbols = symbols

    def spin(self) -> list[tuple[str, int]]:
        """
        Simulates a spin of a slot machine.

        returns the payout 
        """

        return [random.choice(list(self.symbols.items())) for _ in range(3)]

    def calculate_payout(self, spin: list[tuple[str, int]], bet_amount: int) -> int:
        
        return bet_amount * (spin[0] == spin[1] == spin[2])


if __name__ == '__main__':

    symbols = {
        'seven': 1000,
        'cherry': 500,
        'apple': 250
    }


    prize = 0
    game = Slots(int(time.time()), symbols)
    while not prize:
        print(prize)
        choices = game.spin()
        prize = game.calculate_payout(choices, 500)
    print(prize)

