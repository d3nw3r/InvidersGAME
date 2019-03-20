import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # initialization game, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # создание корабля
    ship = Ship(ai_settings, screen)
    # создвние группы для хранени пуль
    bullets = Group()

    # run main code
    while True:
        # отслеживание событий клавиатуры и мыши
        gf.chek_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # удаление пуль вышедших за край
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
