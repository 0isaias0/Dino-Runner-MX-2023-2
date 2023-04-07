import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    MIN_Y_POS = 100
    MAX_Y_POS = 300
    SPEED = 20

    def __init__(self):
        self.image = random.choice(BIRD)
        super().__init__(self.image)
        self.rect.y = random.randint(self.MIN_Y_POS, self.MAX_Y_POS)
        self.speed = self.SPEED 

    def update(self, game_speed, player):
        self.rect.x -= (game_speed + self.speed)
        if self.rect.colliderect(player.dino_rect):
           if not player.shield:
               player.dino_dead = True
           if player.hammer:
               player.dino_dead = False
               
               


