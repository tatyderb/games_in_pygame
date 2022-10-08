class Deck:
    """Колода карт UNO"""
    pass


class Heap:
    """Сброс, верхняя карта открыта"""
    pass


class Player:
    pass


class UnoApplication:
    DEFAULT_HAND_SIZE = 7
    def __init__(self, player_names, hand_size=DEFAULT_HAND_SIZE):
        """Подготовка к игре:
        * Каждому игроку сдается 7 карт
        * 1 карта открывается и начинает сброс.
        * остальные карты кладутся в колоду в закрытую
        """
        self.deck = Deck()
        self.players = [Player(name, self.deck.draw(hand_size)) for name in player_names]
        self.heap = Heap(self.deck.draw(1))

    def run(self):
        """Сама игра в процессе до конца"""
        pass


app = UnoApplication(['Alice', 'Bob'], hand_size=2)
app.run()
