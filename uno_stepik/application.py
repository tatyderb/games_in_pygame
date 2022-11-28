import pygame

import pygame

from uno_stepik.config import GEOM, RSC
from uno_stepik.game_view import GameView

FPS = RSC['FPS']


class Application:
    def __init__(self, filename=None):
        pygame.init()
        size = GEOM['display']
        self.display = pygame.display.set_mode(size)
        pygame.display.set_caption(RSC['title'])
        # icon_img = pygame.image.load(RSC['img']['icon'])
        # pygame.display.set_icon(icon_img)
        self.vgame = GameView(size, self.display)

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.vgame.model_update()
            self.vgame.redraw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.vgame.event_process(event)

            clock.tick(FPS)     # ждать 1/FPS секунды


app = Application()
app.run()
