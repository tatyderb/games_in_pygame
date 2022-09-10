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


# флаг, что приложение работает
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # изменение положения объектов
    player_x += player_dx

    # рисуем на экране
    display.fill('black', (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    pygame.display.update()

