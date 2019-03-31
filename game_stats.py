class GameStats():
    """отслеживание статистики для игры"""
    def __init__(self, ai_settings):
        """инициализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # игра запускаеться в неактивном состоянии
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ship_left = self.ai_settings.ship_limit