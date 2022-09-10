import pygame

pygame.init()

# загружаем изображения
player_img = pygame.image.load('resources/img/player.png')
icon_img = pygame.image.load('resources/img/ufo.png')
bullet_img = pygame.image.load('resources/img/bullet.png')


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

def model_update():
    player_update()
    bullet_update()

def bullet_create():
    """Создаем пулю над игроком, она летит вертикально вверх"""
    global bullet_alive
    x = player_x
    y = player_y - bullet_height
    bullet_alive = True
    return x, y



# перерисовки
def display_redraw():
    display.fill((0, 0, 0), (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    if bullet_alive:
        display.blit(bullet_img, (bullet_x, bullet_y))
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
        event_player(event)
        event_bullet(event)
    return running_status


running = True
while running:
    model_update()
    display_redraw()
    running = event_process()


