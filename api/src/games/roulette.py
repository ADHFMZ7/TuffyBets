import random
import time

class Roulette:

    def __init__(self, seed: int):
        """
        Initializes the roulette wheel with numbers and colors.
        """
        self.wheel = {
            0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black',
            5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red',
            10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red',
            15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red',
            20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black',
            25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black',
            30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red',
            35: 'black', 36: 'red'
        }

        if seed: random.seed(seed)

    def spin(self):
        """
        Simulates spinning the roulette wheel.

        Returns:
            A tuple of (number, color).
        """
        number = random.randint(0, 36)
        color = self.wheel[number]

        return number, color

    def bet_color(self, color: str, bet_amount: int) -> int:
        """
        Place a bet on a color and calculate the outcome.

        Parameters:
            color: The color to bet on ('red' or 'black').
            bet_amount: The amount of money to bet.

        Returns:
            The result of the bet, either 0 (loss) or 2x bet amount (win). Along with the Spun values.
        """
        spun_number, spun_color = self.spin()

        if spun_color == color:
            return bet_amount * 2, spun_number, spun_color
        
        return 0, spun_number, spun_color

    def bet_number(self, number: int, bet_amount: int) -> int:
        """
        Place a bet on a specific number and calculate the outcome.

        Parameters:
            number: The number to bet on (0-36).
            bet_amount: The amount of money to bet.

        Returns:
            The result of the bet, either 0 (loss) or 36x bet amount (win). Along with the Spun values.
        """
        spun_number, spun_color = self.spin()

        if spun_number == number:
            return bet_amount * 36, spun_number, spun_color
        
        return 0, spun_number, spun_color


if __name__ == '__main__':
    roulette_game = Roulette(time.time())

    betted_number = 17
    bet_amount = 50
    winnings = 0

    # Loops until wins
    while True:
        winnings, spun_number, spun_color = roulette_game.bet_number(betted_number, bet_amount)

        if winnings > 0: 
            break   

    print(f"You betted {bet_amount} coins on {betted_number}.\nThe Roulette spun and landed on {spun_number} {spun_color}.\nYou made {winnings - bet_amount} coins.")

    
