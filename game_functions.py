import sys
import pygame


def chek_keydown_event(event, ship):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def chek_keyup_event(event, ship):
    """Реагирует на отпускание клавиши"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def chek_events(ship):
    """обробатывает нажатие клавишы и события от мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            chek_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship):
    # заполняем экран цветом bg_color
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # отображение последнего прорисованого экрана
    pygame.display.flip()

