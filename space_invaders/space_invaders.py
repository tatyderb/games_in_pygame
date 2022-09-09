import pygame as pygame
print(pygame.version.ver)

pygame.init()

# Размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)

# изображения
icon_img = pygame.image.load('resources/img/ufo.png')
player_img = pygame.image.load('resources/img/player.png')

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
player_speed = 4
player_dx = player_speed

# флаг, что приложение работает
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_x += player_dx

    display.blit(player_img, (player_x, player_y))

    pygame.display.update()
