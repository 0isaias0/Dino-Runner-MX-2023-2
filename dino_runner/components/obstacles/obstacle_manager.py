import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cantus import BigCactus
from dino_runner.components.obstacles.bird import Bird



class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        

    def update(self, game_speed, player):
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.rect.x > -obstacle.rect.width]
        if not self.obstacles:
            new_obstacle = random.choice([Cactus(), BigCactus(), Bird()])
            self.obstacles.append(new_obstacle)
        for obstacle in self.obstacles:
            obstacle.update(game_speed, player)
            if obstacle.rect.colliderect(player.dino_rect) and player.hammer:
                self.obstacles.remove(obstacle)

            
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

