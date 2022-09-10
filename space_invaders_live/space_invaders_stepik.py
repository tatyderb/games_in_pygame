import pygame

pygame.init()

# загружаем изображения
icon_img = pygame.image.load('resources/img/ufo.png')
player_img = pygame.image.load('resources/img/player.png')

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

# изменение положения объектов
def player_update():
    global player_x
    player_x += player_dx

def model_update():
    player_update()


# перерисовка объектов
def display_redraw():
    # рисуем на экране
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
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


def event_close_application(event):
    return event.type == pygame.QUIT


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
