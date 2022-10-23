from __future__ import annotations


class Card:

    COLORS = ['red', 'green', 'blue', 'yellow']
    NUMBERS = list(range(0, 10)) + list(range(1, 10))

    # {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow'}
    SHORT_FORM = {color[0]: color for color in COLORS}

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        """ Возвращает строку вида r3 """
        return f'{self.color[0]}{self.number}'

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number

    @staticmethod
    def create(short_form: str) -> Card:
        """ Из строки 'r3' делает карту Card('red', 3) """
        color_letter = short_form[0]
        number = int(short_form[1])
        return Card(Card.SHORT_FORM[color_letter], number)

    @staticmethod
    def list_from_str(text: str) -> list[Card]:
        """ Из строки 'r3 y5 g0' делает [Card('red', 3), Card('yellow', 5), Card('green', 0)] """
        return [Card.create(s) for s in text.split()]





