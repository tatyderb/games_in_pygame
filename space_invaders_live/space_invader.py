import pygame
import random

pygame.init()

# ДЛЯ ОТЛАДКИ, потом убрать
random.seed(10)

# загружаем изображения
player_img = pygame.image.load('resources/img/player.png')
icon_img = pygame.image.load('resources/img/ufo.png')
bullet_img = pygame.image.load('resources/img/bullet.png')
enemy_img = pygame.image.load('resources/img/enemy.png')


# размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)
# print(f'{display_width=} {display_height=} {display_size=}')

# создаем окно
display = pygame.display.set_mode(display_size)
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon_img)

# игрок
player_width = player_img.get_width()
player_height = player_img.get_height()
player_gap = 10
player_x = display_width // 2 - player_width // 2
player_y = display_height - player_height - player_gap
player_speed = 0.5
player_dx = 0

# пуля
bullet_alive = False
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x, bullet_y = 0, 0
# x, y = y, x
bullet_dy = 1

# враг
enemy_alive = False
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()
enemy_x, enemy_y = 0, 0
enemy_dx, enemy_dy = 0, 0

# game over
game_over_status = False

# обновление моделей
def player_update():
    global player_x
    player_x += player_dx  # player_x = player_x + player_dx
    # не дадим игроку выходить за пределы окна
    if player_x < 0:
        player_x = 0
    if player_x > display_width - player_width:
        player_x = display_width - player_width

def bullet_update():
    global bullet_y
    if not bullet_alive:
        return
    bullet_y -= bullet_dy

def collision(x, y, width, height):
    """враг столкнулся с указанным объектом (передан прямоугольник)"""
    rect_enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    rect_other = pygame.Rect(x, y, width, height)
    return rect_enemy.colliderect(rect_other)

def enemy_update():
    global enemy_alive, enemy_x, enemy_y, enemy_dx, enemy_dy
    if not enemy_alive:
        enemy_x, enemy_y, enemy_dx, enemy_dy = enemy_create()
    enemy_x += enemy_dx
    enemy_y += enemy_dy
    # print(f'{enemy_alive} : {enemy_x} {enemy_y} {enemy_dx} {enemy_dy}')

    # столкновение с игроком
    if collision(player_x, player_y, player_width, player_height):
        enemy_alive = False
        game_over()

def model_update():
    player_update()
    bullet_update()
    enemy_update()

def bullet_create():
    """Создаем пулю над игроком, она летит вертикально вверх"""
    global bullet_alive
    x = player_x
    y = player_y - bullet_height
    bullet_alive = True
    return x, y

def enemy_create():
    """Создаем врага в случайном месте, он случайно летит наискосок вниз"""
    global enemy_alive
    # x = random.randint(0, display_width)
    x = player_x
    y = 30

    # dx = random.randint(-2, 3)
    # dy = random.randint(1, 3) / 2
    dx = 0
    dy = 0.1

    enemy_alive = True
    return x, y, dx, dy

def game_over():
    global game_over_status
    game_over_status = True


# перерисовки
def display_redraw():
    display.fill((0, 0, 0), (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    if bullet_alive:
        display.blit(bullet_img, (bullet_x, bullet_y))
    if enemy_alive:
        display.blit(enemy_img, (enemy_x, enemy_y))
    pygame.display.update()

# события
def event_quit(event):
    return event.type != pygame.QUIT

def event_player(event):
    global player_dx
    # нажали клавишу
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_dx = -player_speed
        elif event.key == pygame.K_RIGHT:
            player_dx = player_speed
    # отпустили клавишу
    if event.type == pygame.KEYUP:
        player_dx = 0

def event_bullet(event):
    global bullet_x, bullet_y, bullet_alive
    if event.type == pygame.MOUSEBUTTONDOWN:
        key = pygame.mouse.get_pressed()
        if key[0] and not bullet_alive:
            bullet_x, bullet_y = bullet_create()

def event_process():
    running_status = True
    for event in pygame.event.get():
        running_status = event_quit(event)
        if game_over_status:
            continue
        event_player(event)
        event_bullet(event)
    return running_status


running = True
while running:
    model_update()
    display_redraw()
    running = event_process()


