import pygame
import random

print(pygame.version.ver)

pygame.init()

# Размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)

# изображения
icon_img = pygame.image.load('resources/img/ufo.png')
player_img = pygame.image.load('resources/img/player.png')
enemy_img = pygame.image.load('resources/img/enemy.png')

# создаем окно
display = pygame.display.set_mode(display_size)
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon_img)

# позиция игрока
player_width = player_img.get_width()
player_height = player_img.get_height()
player_gap = 30                                     # расстояние от игрока до низа окна
player_x = display_width // 2 - player_width // 2   # будет потом меняться
player_y = display_height - player_height - player_gap
# print(f'{player_x=} {player_y=}')
player_speed = 1
player_dx = 0

# позиция врага
enemy_alive = False                     # есть враг True или уже убит False (убит - создать нового)
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x, enemy_y, enemy_dx, enemy_dy = 0, 0, 0, 0

def enemy_create():
    """Возвращает случайные координаты и скорость для создания врага"""
    x = random.randrange(0, display_width - enemy_width)
    y = 30

    dx = random.randrange(-2, 3)
    dy = random.randrange(1, 3) / 2

    return x, y, dx, dy


def player_update():
    """Обновляет позицию игрока, врагов, пуль и тп."""
    global player_x
    player_x += player_dx
    # не дадим игроку выходить за пределы экрана

    if player_x < 0:
        player_x = 0

    if player_x + player_width > display_width:
        player_x = display_width - player_width


def enemy_update():
    """Обновляет позицию врага. Если его нет, создает.
    """
    global enemy_x, enemy_y, enemy_dx, enemy_dy, enemy_alive
    if not enemy_alive:
        enemy_x, enemy_y, enemy_dx, enemy_dy = enemy_create()
        enemy_alive = True
    enemy_x += enemy_dx
    enemy_y += enemy_dy


def model_update():
    player_update()
    enemy_update()

def display_redraw():
    """Перерисовывает все элементы"""
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    if enemy_alive:
        display.blit(enemy_img, (enemy_x, enemy_y, enemy_width, enemy_height))

    pygame.display.update()

def event_close_application(event):
    """Закрываем окно по нажатию крестика"""
    running = event.type == pygame.QUIT
    return running

def event_player(event):
    """Вправо-влево по нажатию стрелок и a, d;"""
    global player_dx
    if event.type == pygame.KEYDOWN:
        if event.key in (pygame.K_LEFT, pygame.K_a):
            player_dx = -player_speed
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            player_dx = player_speed

    if event.type == pygame.KEYUP:
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT,
                         pygame.K_a, pygame.K_d):
            player_dx = 0


def event_process():
    """Обрабатывает события клавиатуры и мыши, возвращает False, если приложение хотят закрыть."""
    for event in pygame.event.get():
        event_player(event)
        if event_close_application(event):
            return False
    return True

# флаг, что приложение работает
running = True
while running:
    model_update()
    display_redraw()
    running = event_process()




