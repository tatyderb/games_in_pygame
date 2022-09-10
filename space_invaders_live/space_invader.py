import pygame

pygame.init()

# загружаем изображения
player_img = pygame.image.load('resources/img/player.png')
icon_img = pygame.image.load('resources/img/ufo.png')


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
player_speed = 1
player_dx = player_speed

# обновление моделей
def player_update():
    global player_x
    player_x += player_dx  # player_x = player_x + player_dx

def model_update():
    player_update()

# перерисовки
def display_redraw():
    display.fill((0, 0, 0), (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    pygame.display.update()

# события
def event_quit(event):
    return event.type != pygame.QUIT

def event_process():
    running_status = True
    for event in pygame.event.get():
        running_status = event_quit(event)
    return running_status


running = True
while running:
    model_update()
    display_redraw()
    running = event_process()


