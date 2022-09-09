import pygame as pygame
print(pygame.version.ver)

pygame.init()

# Размеры окна
display_width = 800
display_height = 600
display_size = (display_width, display_height)

# создаем окно
pygame.display.set_mode(display_size)
