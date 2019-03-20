import sys
import pygame
from bullet import Bullet


def chek_keydown_event(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # создание новой пули и включение ее в группу
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def chek_keyup_event(event, ship):
    """Реагирует на отпускание клавиши"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def chek_events(ai_settings, screen, ship, bullets):
    """обробатывает нажатие клавишы и события от мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    # заполняем экран цветом bg_color
    screen.fill(ai_settings.bg_color)
    # все пули выводятся позади корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # отображение последнего прорисованого экрана
    pygame.display.flip()

