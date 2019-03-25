import pygame
from settings import Settings
from ship import Ship
from alien import Alien
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
    # создание пришельца
    alien = Alien(ai_settings, screen)
    # создвние группы для хранени пуль и группы пришельцев
    bullets = Group()
    aliens = Group()
    # создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # run main code
    while True:
        # отслеживание событий клавиатуры и мыши
        gf.chek_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
