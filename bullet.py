import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями выпущеными кораблем"""
    def __init__(self, ai_settings, screen, ship):
        """Создает обект пули в текущей позиции корабля"""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначении правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули хранитися в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """перемещает пулю вверх по экрану"""
        self.y -= self.speed_factor
        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
