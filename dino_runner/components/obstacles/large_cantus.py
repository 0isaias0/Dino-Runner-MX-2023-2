import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS

class BigCactus(Obstacle):
    Y_POS_CACTUS = 300

    def __init__(self):
        self.image = random.choice(LARGE_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS
        
