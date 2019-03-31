import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # initialization game, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # создание кнопки Button
    play_button = Button(ai_settings, screen, "Play")
    # создание корабля
    ship = Ship(ai_settings, screen)
    # создание пришельца
    alien = Alien(ai_settings, screen)
    # создвние группы для хранени пуль и группы пришельцев
    bullets = Group()
    aliens = Group()
    # создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)

    # run main code
    while True:
        # отслеживание событий клавиатуры и мыши
        gf.chek_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
