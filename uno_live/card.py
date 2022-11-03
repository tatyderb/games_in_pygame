from __future__ import annotations


COLORS = ('red', 'green', 'yellow', 'blue')
NUMBERS = tuple(list(range(0, 10)) + list(range(1, 10)))


class Card:

    def __init__(self, color: str, number: int | str):
        self.color = color
        self.number = number

    def __repr__(self) -> str:
        """Возвращаем строку вида 3r"""
        return f'{self.color[0]}{self.number}'

    def playable(self, top: Card) -> bool:
        """Можно ли играть карту self на карту top"""
        return self.color == top.color or self.number == top.number

    def __eq__(self, other: Card) -> bool:
        """Для работы self == other"""
        return self.color == other.color and self.number == other.number

    @staticmethod
    def all_cards() -> list[Card]:
        return [Card(color, number) for color in COLORS for number in NUMBERS]

    @staticmethod
    def list_from_str(text: str = '') -> list[Card]:
        """По строке вида 'r3 g7 y1' делаю список карт"""
        card_list = []
        # {'r': 'red', 'g':'green', ...}
        color_dict = {color[0]: color for color in COLORS}
        for card in text.split():
            short_color = card[0]
            number = int(card[1])
            card_list.append(Card(color_dict[short_color], number))
        return card_list


