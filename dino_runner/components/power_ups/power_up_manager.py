import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.god_mode import GodMode


class PowerUpManager:
    POINTS = 200

    def __init__(self):
        self.power_ups = []

    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0 and points % self.POINTS == 0:
            new_power_up = random.choice([Shield(), Hammer(), GodMode()])
            self.power_ups.append(new_power_up)

        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.pop()
            if power_up.used:
                player.set_power_up(power_up)
            power_up.update(game_speed, player)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)