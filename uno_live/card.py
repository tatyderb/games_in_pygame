class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        """Возвращаем строку вида 3r"""
        return f'{self.color[0]}{self.number}'

    def playable(self, top):
        """Можно ли играть карту self на карту top"""
        return self.color == top.color or self.number == top.number

    def __eq__(self, other):
        """Для работы self == other"""
        return self.color == other.color and self.number == other.number


