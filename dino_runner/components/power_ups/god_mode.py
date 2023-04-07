
import random
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import FLY, FLY_TYPE
class GodMode(PowerUp):
    MIN_Y_POS = 125
    MAX_Y_POS = 300


    def __init__(self):
        self.image = FLY
        self.type = FLY_TYPE
        super().__init__(self.image, self.type)
        self.rect.y = random.randint(self.MIN_Y_POS, self.MAX_Y_POS)
        self.speed = 0

 
        
       