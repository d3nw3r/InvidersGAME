class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализация настроек игры"""
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # настройка скорости корабля
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # настройка пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение в право а -1 влево
        self.fleet_direction = 1
        # темп ускорения игры
        self.speedup_scale = 1.1
        # темп роста стоимости пришельца
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """инициализирует настройки изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1
        # подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """увеличивает настройки скорости и стоимости пришельца"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
