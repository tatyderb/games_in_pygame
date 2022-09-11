import pygame

pygame.init()

# загружаем изображения
icon_img = pygame.image.load('resources/img/ufo.png')
player_img = pygame.image.load('resources/img/player.png')
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

# позиция игрока
player_width = player_img.get_width()
player_height = player_img.get_height()
player_gap = 10                                     # расстояние от игрока до низа окна
player_x = display_width // 2 - player_width // 2   # будет потом меняться
player_y = display_height - player_height - player_gap
player_speed = 1
player_dx = player_speed

# пуля
bullet_alive = False
bullet_width = bullet_img.get_width()
bullet_height = bullet_img.get_height()
bullet_x, bullet_y, bullet_dy = 0, 0, 0
bullet_speed = 5


# изменение положения объектов
def player_update():
    """Обновляет позицию игрока."""
    global player_x
    player_x += player_dx

    # не дадим игроку выходить за пределы экрана
    if player_x < 0:
        player_x = 0

    if player_x + player_width > display_width:
        player_x = display_width - player_width

def bullet_create():
    """Возвращает координаты пули"""
    x = player_x + player_width / 2 - bullet_width / 2
    y = player_y - bullet_height
    dy = -bullet_speed
    return x, y, dy

def bullet_update():
    global bullet_y
    if bullet_alive:
        bullet_y += bullet_dy


def model_update():
    player_update()


# перерисовка объектов
def display_redraw():
    # рисуем на экране
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    if bullet_alive:
        display.blit(bullet_img, (bullet_x, bullet_y))

    pygame.display.update()

# обработка событий
def event_player(event):
    """Вправо-влево по нажатию стрелок и a, d;"""
    global player_dx
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            player_dx = -player_speed
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            player_dx = player_speed

    # отпускаем эти кнопки и останавливаемся
    if event.type == pygame.KEYUP:
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT,
                         pygame.K_a, pygame.K_d):
            player_dx = 0

def event_bullet(event):
    """Стреляет по нажатию левой кнопки мыши."""
    global bullet_alive, bullet_x, bullet_y, bullet_dy
    if event.type == pygame.MOUSEBUTTONDOWN:
        key = pygame.mouse.get_pressed()
        print(f'{key=} {bullet_alive=}')
        if key[0] and not bullet_alive:
            bullet_x, bullet_y, bullet_dy = bullet_create()
            bullet_alive = True

def event_close_application(event):
    return event.type == pygame.QUIT


def event_process():
    """Обрабатывает события клавиатуры и мыши, возвращает False, если приложение хотят закрыть."""
    for event in pygame.event.get():
        event_player(event)
        event_bullet(event)
        if event_close_application(event):
            return False
    return True


# флаг, что приложение работает
running = True
while running:
    model_update()
    display_redraw()
    running = event_process()
