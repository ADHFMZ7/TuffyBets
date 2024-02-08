import random

class DailySpin:
    
    def __init__(self):
        self.prizes = ['200 Coins', '100 Coins', '50 Coins', '10 Coins', 'No Luck'] # convert to use of values
        
    def spin_wheel(self, seed: int = 0) -> int:
        if seed: random.seed(seed)
        spin_result = random.choice(self.prizes)
        return spin_result

game = DailySpin()
result = game.spin_wheel()
print("You spun the wheel and got:", result)
