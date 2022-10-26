from __future__ import annotations

from uno_stepik.card import Card


class CardList:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def __repr__(self):
        return ' '.join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def add(self, card: Card):
        """ Добавить карту в КОНЕЦ списка. """
        self.cards.append(card)


class Deck(CardList):
    def __init__(self, cards: list[Card]):
        super(Deck, self).__init__(cards)

    def draw(self) -> Card:
        """ Взять 1 карту"""
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card


class Heap(CardList):
    def __init__(self, cards: list[Card]):
        super(Heap, self).__init__(cards)

    def __str__(self):
        return str(self.top())

    def top(self) -> Card:
        """ Верхняя карта """
        return self.cards[-1]


class Hand(CardList):
    def __init__(self, cards: list[Card]):
        super(Hand, self).__init__(cards)

    def playable_cards(self, top: Card) -> list[Card]:
        return [card for card in self.cards if card.playable(top)]

    def remove(self, card: Card):
        self.cards.remove(card)
