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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_x = player_x + player_dx

    display.fill((0, 0, 0), (0, 0, display_width, display_height))
    display.blit(player_img, (player_x, player_y))
    pygame.display.update()
