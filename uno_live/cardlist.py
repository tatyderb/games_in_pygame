from card import Card

import random

COLORS = ('red', 'green', 'yellow', 'blue')
NUMBERS = tuple(list(range(0, 10)) + list(range(1, 10)))


class Deck:
    """Колода карт UNO"""
    def __init__(self):
        self.cards = []

    @staticmethod
    def generate(colors=COLORS, numbers=NUMBERS):
        deck = Deck()
        for color in colors:
            for number in numbers:
                deck.add(Card(color, number))
        return deck

    @staticmethod
    def create(card_list):
        deck = Deck()
        for card in card_list:
            deck.add(card)
        return deck

    @staticmethod
    def create_from_string(card_list_as_string=''):
        """По строке вида 'r3 g7 y1' делаю колоду"""
        deck = Deck()
        # {'r': 'red', 'g':'green', ...}
        color_dict = {color[0]: color for color in COLORS}
        for card in card_list_as_string.split():
            short_color = card[0]
            number = int(card[1])
            deck.add(Card(color_dict[short_color], number))
        return deck

    def add(self, card):
        self.cards.append(card)

    def draw(self, size=1):
        """Возвращает или список карт длины size, или одну карту, если size=1.
        Эти карты удаляются из колоды.
        """

        out = self.cards[:size]
        self.cards = self.cards[size:]
        if size == 1:
            out = out[0]
        return out

    def __repr__(self):
        # h, m, s = '12:05:33'.split(':')
        # s = ':'.join(['12', '05', '33'])    # s = '12:05:33'
        s = ' '.join([str(card) for card in self.cards])
        return s

    def shuffle(self):
        """Перемешивает колоду"""
        random.shuffle(self.cards)


class Heap:
    """Сброс, верхняя карта (последняя в списке) открыта"""
    def __init__(self, card):
        self.cards = [card]

    def __repr__(self):
        return f'Top: {self.top()}'

    def top(self):
        return self.cards[-1]

    def add(self, card):
        self.cards.append(card)


class Hand:
    """Рука игрока"""
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return ' '.join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def remove(self, removable_card):
        """Удалить карту с руки removable_card"""
        self.cards.remove(removable_card)

    def playable_list(self, top):
        """Возвращает список карт, подходящих для игры на top"""
        return [card for card in self.cards if card.playable(top)]

    def add(self, card):
        self.cards.append(card)
