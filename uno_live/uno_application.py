from cardlist import Deck, Heap
from uno_live.player import Player


class UnoGame:
    DEFAULT_HAND_SIZE = 7

    def __init__(self, player_names, hand_size=DEFAULT_HAND_SIZE, deck=None):
        """Подготовка к игре:
        * Каждому игроку сдается 7 карт
        * 1 карта открывается и начинает сброс.
        * остальные карты кладутся в колоду в закрытую
        """
        if deck is None:
            self.deck = Deck()
        else:
            self.deck = deck
        self.players = [Player(name, self.deck.draw(hand_size)) for name in player_names]
        self.player_index = 0
        self.player_size = len(self.players)
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

        if len(current.hand) == 0:
            # текущий игрок сборосил все карты, игра закончена
            return False

        # ход переходит другому игроку
        # 2: 0 1 0 1 0 1
        # 3:  0 1 2 0 1 2 0 1 2
        # +1: 0 1 2 3 4 5 6 7 8
        # %3: 0 1 2 0 1 2 0 1 2
        self.player_index = (self.player_index + 1) % self.player_size
        # игра продолжается
        return True

    def congratulation_winner(self):
        print(f'Игрок {self.current_player().name} победил!')

    def current_player(self):
        return self.players[self.player_index]


# r3 r5 - Alice
# b1 g2 - Bob
# g3 - heap
# y9 - deck
d = Deck.create_from_string('r3 r5 b1 g2 g3 y9')
app = UnoGame(['Alice', 'Bob'], hand_size=2, deck=d)
app.run()
