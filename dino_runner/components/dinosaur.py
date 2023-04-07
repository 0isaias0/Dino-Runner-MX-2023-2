import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.god_mode import GodMode
from dino_runner.utils.constants import (RUNNING, RUNNING_SHIELD, RUNNING_HAMMER,
                                         DUCKING, DUCKING_SHIELD, DUCKING_HAMMER,
                                         JUMPING, JUMPING_SHIELD, JUMPING_HAMMER,
                                         DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE,
                                         DEAD, FLY, FLY_TYPE)

class Dinosaur:
    POS_X = 80
    POS_Y = 310
    POS_Y_DUKING = 340
    JUMP_VEL = 8.5
 
 
    def __init__(self):
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, FLY_TYPE: RUNNING}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, FLY_TYPE: DUCKING}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, FLY_TYPE: FLY}
        self.dead_img = DEAD
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False 
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.shield = False
        self.hammer = False
        self.god = False
        self.time_up_power_up = 0
        

    

    def update(self, user_input, game_speed, player):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_dead:
            self.dead()

        

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
            self.dino_dead = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_dead = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
            self.dino_dead = False

        if self.god:
            cursor_pos = pygame.mouse.get_pos()
            
            self.dino_rect.x = cursor_pos[0]
            self.dino_rect.y = cursor_pos[1]
        

            

            

        if user_input[pygame.K_SPACE] and self.hammer:
            self.throw_hammer()

        if self.step_index >= 10:
            self.step_index = 0

        if self.shield:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                 self.reset()
        if self.hammer:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.reset()
        if self.god:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.reset()


                

    def draw(self, screen):    
        screen.blit(self.image, self.dino_rect)

    def throw_hammer(self):
        hammer = Hammer()
        hammer.rect.x = self.dino_rect.x + self.dino_rect.width
        hammer.rect.y = self.dino_rect.y + self.dino_rect.height / 2
        hammer.vel_x = 10
        

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X 
        self.dino_rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
        

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X 
        self.dino_rect.y = self.POS_Y_DUKING 
        self.step_index += 1

    def dead(self):
        self.image = self.dead_img
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self. POS_X
        self.dino_rect.y = self.POS_Y
      

    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.shield = True
            self.type = SHIELD_TYPE
            self.time_up_power_up = power_up.time_up
        if power_up.type == HAMMER_TYPE:
            self.hammer = True
            self.type = HAMMER_TYPE
            self.time_up_power_up = power_up.time_up
        if power_up.type == FLY_TYPE:
            self.god = True
            self.type = FLY_TYPE
            self.time_up_power_up = power_up.time_up


    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.hammer = False
        self.god = False
        self.time_up_power_up = 0
