import pygame

pygame.init()

# загружаем изображения
icon_img = pygame.image.load('resources/img/ufo.png')

# размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)
# print(f'{display_width=} {display_height=} {display_size=}')

# создаем окно
pygame.display.set_mode(display_size)
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon_img)

# флаг, что приложение работает
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


