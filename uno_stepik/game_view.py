from __future__ import annotations

import pygame

from uno_stepik.card import Card
from uno_stepik.card_view import CardView
from uno_stepik.config import GEOM, RSC


class GameView:
    def __init__(self, size, display):
        # отладим с одной отрисованной картой
        self.cv = CardView(Card('red', 4), 10, 50)
        self.width, self.height = size
        self.display = display
        
    def redraw(self):
        self.display.fill((0, 81, 44), (0, 0, self.width, self.height))
        self.cv.redraw(self.display)
        pygame.display.update()

    def model_update(self):
        pass

    def event_process(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # нажата левая кнопка
            # 0 - 1 - 2
            # 0 - 1 - 2 - 3 - 4
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if self.cv.r().collidepoint(x, y):
                    self.cv.flip()
                    self.redraw()
