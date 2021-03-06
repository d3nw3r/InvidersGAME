import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def chek_keydown_event(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def chek_keyup_event(event, ship):
    """Реагирует на отпускание клавиши"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def chek_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """обробатывает нажатие клавишы и события от мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            chek_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            chek_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def chek_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """запускаем новую игру при нажатии на плей"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # сброс игровых настроек
        ai_settings.initialize_dynamic_settings()
        # указатель миши скрывается
        pygame.mouse.set_visible(False)
        # сброс игоровой статистики
        stats.reset_stats()
        stats.game_active = True
        # сброс изображения счета и уровня
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        # очистка списка пуль и пришельцев
        aliens.empty()
        bullets.empty()
        # создание нового флота и размещение корабля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sb.prep_ships()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # заполняем экран цветом bg_color
    screen.fill(ai_settings.bg_color)
    # вывод счета
    sb.show_score()
    # все пули выводятся позади корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # кнопка плей отображается в том случае если игра не активна
    if not stats.game_active:
        play_button.draw_button()
    # отображение последнего прорисованого экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """обновляет позиции пуль и уничтожает старые пули"""
    # обновление позиции пуль
    bullets.update()

    # удаление пуль вышедших за край
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # проверка попадания в пришельцев
    # при обнаружении попадания удалить пулю и пришельца
    chek_bullet_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def chek_bullet_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Обработка колизий пуль с пришельцами"""
    # удаление пуль и пришельцев участвующих в колизии
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
            chek_high_score(stats, sb)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """выпускает пулю если максимум еще не достигнут"""
    # создание новой пули и включение ее в группу
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляется количество пришлеьцев в ряду"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов помещающихся на экране"""
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """создает флот пришельцев"""
    # создвние пришельцев и вычисление их в ряду
    # интервал между пришельцами равен ширине одного пришельца
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # создание пришельца и размещение его в ряду
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def chek_fleet_edges(ai_settings, aliens):
    """реагирует на достижение пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.chek_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """опускает весь флот и меняет направление флота"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):

    """обробатывает столкновение коробля с пришельцем"""
    if stats.ship_left > 0:
        stats.ship_left -= 1
        # обновление игровой информации
        sb.prep_ships()
        # очистка списка пришельцев и пуль
        aliens.empty()
        bullets.empty()

        # создание нового флота и размещение нового коробля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # пауза
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def chek_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """проверяет добрались ли пришельці до нижнего края"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # происходит тоже что и со столкновением коробля
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """  проверяет достиг ли флот края экрана затем обновляет позиции всех пришельцев во флоте"""
    chek_fleet_edges(ai_settings, aliens)
    aliens.update()

    # проверка колизий "пришелец-корабель"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    chek_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def chek_high_score(stats, sb):
    """проверяте появился ли новый рекорд"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
