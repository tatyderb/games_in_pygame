from card import Card

import random


class CardList:

    def __init__(self, cards: list):
        self.cards = cards

    def __repr__(self):
        # h, m, s = '12:05:33'.split(':')
        # s = ':'.join(['12', '05', '33'])    # s = '12:05:33'
        s = ' '.join([str(card) for card in self.cards])
        return s

    def add(self, card: Card):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)


class Deck(CardList):
    """Колода карт UNO"""
    def __init__(self, cards: list):
        super().__init__(cards)

    def draw(self, size=1):
        """Возвращает или список карт длины size, или одну карту, если size=1.
        Эти карты удаляются из колоды.
        """

        out = self.cards[:size]
        self.cards = self.cards[size:]
        if size == 1:
            out = out[0]
        return out

    def shuffle(self):
        """Перемешивает колоду"""
        random.shuffle(self.cards)


class Heap(CardList):
    """Сброс, верхняя карта (последняя в списке) открыта"""
    def __init__(self, cards):
        super().__init__(cards)

    def __str__(self):
        """str(heap)"""
        return f'Top: {self.top()}'

    def top(self):
        return self.cards[-1]


class Hand(CardList):
    """Рука игрока"""
    def __init__(self, cards):
        super().__init__(cards)

    def remove(self, removable_card):
        """Удалить карту с руки removable_card"""
        self.cards.remove(removable_card)

    def playable_list(self, top) -> list:
        """Возвращает список карт, подходящих для игры на top"""
        return [card for card in self.cards if card.playable(top)]
