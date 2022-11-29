from __future__ import annotations

import pygame

from uno_stepik.card import Card
from uno_stepik.card_list import Heap, Deck
from uno_stepik.card_view import CardView
from uno_stepik.config import GEOM, RSC
from uno_stepik.game import Game

'''
# черновая прикидка расположения
# AI1  AI2
# TOP  DECK
# PLAYER
'''

# дано в конфигурации геометрии
XGAP = GEOM['xgap']                 # отступ по Х
YGAP = GEOM['ygap']                 # отступ по Y
DWIDTH, DHEIGHT = GEOM['display']   # размер экрана
CW, CH = GEOM['card']               # размер карты

# Y координаты рядов 0, 1, 2
R0Y = YGAP
R1Y = (DHEIGHT - CH) // 2 + YGAP
R2Y = DHEIGHT - CH - YGAP

# Х координаты компонент
PLAYERX = XGAP                      # игрока себя рисуем от левого края
AI1X = XGAP                         # AI1 рисуем от левого края
AI2X = DWIDTH // 2 + XGAP           # AI2 рисуем от центра (с отступом!)
TOPX = DWIDTH // 2 - XGAP - CW      # отбой от центра влево с отступом
DECKX = DWIDTH // 2 + XGAP          # колода от центра вправо с отступом
HAND_WIDTH = DWIDTH - 2 * XGAP      # ширина карт руки интерактивного игрока
COMPACT_HAND_WIDTH = DWIDTH // 2 - 2 * XGAP  # ширина карт AI


class HeapView:
    def __init__(self, heap: Heap, x: int, y: int):
        self.heap = heap
        self.x = x
        self.y = y

    def redraw(self, display: pygame.Surface):
        cv = CardView(self.heap.top(), self.x, self.y)
        cv.redraw(display)


class DeckView:
    def __init__(self, deck: Deck, x: int, y: int):
        self.deck = deck    # пока не используется, на всякий случай
        self.x = x
        self.y = y

    def redraw(self, display: pygame.Surface):
        CardView.redraw_cover(display, self.x, self.y)


class GameView:
    def __init__(self, game: Game, size: tuple[int, int], display: pygame.Surface):
        # отладим с одной отрисованной картой
        # self.cv = CardView(Card('red', 4), 10, 50)
        self.width, self.height = size
        self.display = display

        self.game = game

        # компоненты
        self.vheap = HeapView(game.heap, TOPX, R1Y)
        self.vdeck = DeckView(game.deck, DECKX, R1Y)
        
    def redraw(self):
        self.display.fill((0, 81, 44), (0, 0, self.width, self.height))
        # self.cv.redraw(self.display)
        self.vheap.redraw(self.display)
        self.vdeck.redraw(self.display)
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
                # if self.cv.r().collidepoint(x, y):
                #    self.cv.flip()
                #    self.redraw()
