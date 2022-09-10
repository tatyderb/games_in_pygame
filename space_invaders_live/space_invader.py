import pygame

pygame.init()

# размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)
# print(f'{display_width=} {display_height=} {display_size=}')

# создаем окно
pygame.display.set_mode(display_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
