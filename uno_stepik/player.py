from __future__ import annotations

from uno_stepik.card import Card
from uno_stepik.card_list import Hand


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.hand = Hand(cards)

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': repr(self.hand)
        }

    def get_playable_card(self, top: Card) -> Card | None:
        """ Возвращаем первую подходящую карту для игры на top или None, если подходящих карт нет. """
        playable_cards = self.hand.playable_cards(top)
        if not playable_cards:
            return None
        return playable_cards[0]

    def no_cards(self) -> bool:
        """ True, если в руке нет карт. """
        return len(self.hand) == 0
