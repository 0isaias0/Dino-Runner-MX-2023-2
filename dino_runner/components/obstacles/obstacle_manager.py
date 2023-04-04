from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:

    def __init__(self):
        self.obstacle = []
        

    def update(self, game_speed):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacle.pop()
            obstacle.update(game_speed)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
