import random
from prizes import Prize

class DailySpin:
    
    def __init__(self):
        self.prize_manager = Prize()
        
    def spin_wheel(self) -> tuple[str, int, str]:
        """
        Randomly chooses from prize pool

        """
        spin_result = self.prize_manager.get_random_prize()
        return spin_result

game = DailySpin()
result = game.spin_wheel()
print("You spun the wheel and got:", result)
