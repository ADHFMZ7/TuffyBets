from prizes import PrizePool, Prize

class DailySpin:
    
    def __init__(self):
        self.prize_manager = PrizePool()
        
    def spin_wheel(self) -> Prize:
        """
        Randomly chooses from prize pool

        """
        spin_result = self.prize_manager.get_random_prize()
        return spin_result

game = DailySpin()
result = game.spin_wheel()
print("You spun the wheel and got:", result)
