import pygame

class Ship():

    def __init__(self, screen):
        """Инициализирует корабель и создает его начальную позицию"""
        self.screen = screen
        # загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images//rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый новый корабль появляется у нижнего края окна
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
