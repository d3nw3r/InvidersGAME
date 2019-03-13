import sys
import pygame
from settings import Settings

def run_game():
    # initialization game, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')


    # run main code
    while True:
        # отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # заполняем єкран цветом bg_color
            screen.fill(ai_settings.bg_color)
            # отображение последнего прорисованого экрана
            pygame.display.flip()


run_game()
