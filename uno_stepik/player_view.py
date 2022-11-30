from __future__ import annotations


import pygame

from uno_stepik.card_view import CardView
from uno_stepik.config import GEOM
from uno_stepik.player import Player


DXCARD = GEOM['dx_card']
DXCARD_COMPACT = GEOM['dx_card_compact']


class PlayerView:
    def __init__(self, player: Player, x: int, y: int):
        self.player = player
        self.x = x
        self.y = y
        self.hand_view = []
        self.update_hand()

    def update_hand(self):
        pass

    def redraw(self, display):
        for vcard in self.hand_view:
            vcard.redraw(display)


class PlayerCompactView(PlayerView):
    def update_hand(self):
        DXCARD = DXCARD_COMPACT
        self.hand_view = [CardView(card, self.x + DXCARD * i, self.y)
                          for i, card in enumerate(self.player.hand.cards)]


class PlayerInteractiveView(PlayerView):
    def update_hand(self):
        self.hand_view = [CardView(card, self.x + (DXCARD + CardView.width) * i, self.y)
                          for i, card in enumerate(self.player.hand.cards)]
