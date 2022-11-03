from __future__ import annotations

import pygame

from uno_live.card import Card
from uno_live.data import GEOM, RSC


class CardView:

    back_img = None
    size = (width, height) = GEOM['card']

    def __init__(self, card: Card, x: int, y: int):
        self.card = card
        self.x = x
        self.y = y

        self.opened = True # лицом или рубашкой рисовать карту

        # создаю изображение карты
        filename = RSC['img']['card'].format(repr(card))
        img = pygame.image.load(filename)
        self.img = pygame.transform.scale(img, self.size)

        # если рубашка еще не загружена, сделать изображение рубашки
        if CardView.back_img is None:
            filename = RSC['img']['back']
            img = pygame.image.load(filename)
            CardView.back_img = pygame.transform.scale(img, self.size)

    def redraw(self, display: pygame.Surface):
        if not self.opened:
            display.blit(self.back_img, (self.x, self.y))
        else:
            display.blit(self.img, (self.x, self.y))

    def r(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def flip(self):
        self.opened = not self.opened
