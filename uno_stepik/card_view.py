from __future__ import annotations

import pygame

from uno_stepik.card import Card
from uno_stepik.config import GEOM, RSC


class CardView:

    back_img = None
    size = (width, height) = GEOM['card']

    def __init__(self, card: Card | None, x: int, y: int, opened: bool = True):
        self.__card = card
        self.__x = x
        self.__y = y

        self.opened = opened                # лицом или рубашкой рисовать карту

        # создаю изображение карты
        if card is None:
            if opened:
                raise ValueError('Unknown card should be opened')
            else:
                self.img = None
        else:
            filename = RSC['img']['card'].format(repr(card))
            img = pygame.image.load(filename)
            self.img = pygame.transform.scale(img, self.size)

        # если рубашка еще не загружена, сделать изображение рубашки
        if CardView.back_img is None:
            filename = RSC['img']['back']
            img = pygame.image.load(filename)
            CardView.back_img = pygame.transform.scale(img, self.size)

    def __repr__(self):
        return f'{self.card}{self.pos}'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val: int):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val: int):
        self.__y = val

    @property
    def pos(self):
        return self.__x, self.__y

    @pos.setter
    def pos(self, val: tuple[int, int]):
        self.x, self.y = val

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, card: Card):
        self.__card = card
        filename = RSC['img']['card'].format(repr(card))
        img = pygame.image.load(filename)
        self.img = pygame.transform.scale(img, self.size)

    def redraw(self, display: pygame.Surface):
        if not self.opened:
            display.blit(self.back_img, (self.x, self.y))
        else:
            if self.img:
                display.blit(self.img, (self.x, self.y))
            else:
                raise ValueError('Unknown card should be draw')

    def r(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def flip(self):
        self.opened = not self.opened
        print('card flip')
