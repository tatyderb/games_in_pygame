class Deck:
    """Колода карт UNO"""
    pass


class Heap:
    """Сброс, верхняя карта открыта"""
    pass


class Hand:
    """Рука игрока"""
    def __init__(self, cards):
        self.cards = cards


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.hand = Hand(cards)


class UnoGame:
    DEFAULT_HAND_SIZE = 7
    def __init__(self, player_names, hand_size=DEFAULT_HAND_SIZE):
        """Подготовка к игре:
        * Каждому игроку сдается 7 карт
        * 1 карта открывается и начинает сброс.
        * остальные карты кладутся в колоду в закрытую
        """
        self.deck = Deck()
        self.players = [Player(name, self.deck.draw(hand_size)) for name in player_names]
        self.player_index = 0
        self.heap = Heap(self.deck.draw(1))

    def run(self):
        """Сама игра в процессе до конца
        """
        is_active = True
        while is_active:
            is_active = self.turn()
        self.congratulation_winner()

    def turn(self):
        """
        Ход игрока:
        * Положи одну карту из руки подходящего цвета или номера или действия.
        * Если подходящей карты нет, возьми карту из колоды в закрытую.
        * Если она подходит, её можно сразу же сыграть.
        :return: False, если у игрока закончились карты (игра окончена).
        """
        top = self.heap.top()
        current = self.current_player()
        card = current.get_payable_card(top)  # убирать карту card из руки
        if card is not None:
            # подходящая карта, кладем в отбой
            self.heap.add(card)
        else:
            # Если подходящей карты нет, возьми карту из колоды в закрытую.
            card = self.deck.draw(1)
            current.add_card(card)
            # * Если она подходит, её можно сразу же сыграть.
            card = current.get_payable_card(top)
            if card is not None:
                # подходящая карта, кладем в отбой
                self.heap.add(card)

        return len(current.hand()) == 0

    def congratulation_winner(self):
        print(f'Игрок {self.current_player().name} победил!')

    def current_player(self):
        return self.players[self.player_index]


app = UnoGame(['Alice', 'Bob'], hand_size=2)
app.run()
