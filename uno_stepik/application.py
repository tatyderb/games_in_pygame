import pygame

import pygame

from uno_stepik.config import GEOM, RSC

FPS = RSC['FPS']


class Application:
    def __init__(self, filename=None):
        pygame.init()
        size = GEOM['display']
        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption(RSC['title'])
        # icon_img = pygame.image.load(RSC['img']['icon'])
        # pygame.display.set_icon(icon_img)

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            # TODO: model_update()
            # TODO: redraw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # TODO: event_process(event)

            clock.tick(FPS)     # ждать 1/FPS секунды


app = Application()
app.run()
