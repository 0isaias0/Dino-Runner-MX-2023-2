import random
from pygame.font import Font
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = "freesansbold.ttf"



def get_message(message, size, width = SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2):
    font = Font(FONT_STYLE, size)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
