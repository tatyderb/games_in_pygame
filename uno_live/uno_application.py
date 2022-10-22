import json

from cardlist import Deck, Heap, Hand
from card import Card
from player import Player


class UnoGame:
    DEFAULT_HAND_SIZE = 7

    def __init__(self):
        self.players = None
        self.player_index = None
        self.player_size = None
        self.deck = None
        self.heap = None

    def __repr__(self):
        return '\n'.join([
            repr(self.deck),
            repr(self.heap),
            str(self.player_index)
        ])


    @staticmethod
    def create(player_names: list, hand_size: int = DEFAULT_HAND_SIZE, deck: Deck | None = None):
        """Подготовка к игре:
        * Каждому игроку сдается 7 карт
        * 1 карта открывается и начинает сброс.
        * остальные карты кладутся в колоду в закрытую
        """
        game = UnoGame()
        if deck is None:
            game.deck = Deck(Card.all_cards())
        else:
            game.deck = deck
        game.deck.shuffle()
        game.players = [Player(name, game.deck.draw(hand_size)) for name in player_names]
        game.player_index = 0
        game.player_size = len(game.players)
        game.heap = Heap([game.deck.draw(1)])
        return game

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
        print(self.heap)
        current = self.current_player()
        print(current)
        card = current.get_payable_card(top)  # убирать карту card из руки
        if card is not None:
            # подходящая карта, кладем в отбой
            print(f'Play {card}')
            self.heap.add(card)
        else:
            # Если подходящей карты нет, возьми карту из колоды в закрытую.
            print('Pass! Берем карту из колоды.')
            card = self.deck.draw(1)
            current.add_card(card)
            # * Если она подходит, её можно сразу же сыграть.
            card = current.get_payable_card(top)
            if card is not None:
                # подходящая карта, кладем в отбой
                self.heap.add(card)
                print(f'Play {card}')

        print(current)

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

    @staticmethod
    def load(gs: dict):
        """
        load game from dict
        game_state = {
            'player_index': 0,
            'players': [
                {
                    'name': 'Charly',
                    'hand': 'r3 r5'
                },
                {
                    'name': 'Bob',
                    'hand': 'b1 g2'
                },

            ],
            'heap': 'r4 g5 g3',
            'deck': 'y9 r9 y0 y1'
        }
        """
        game = UnoGame()
        game.deck = Deck(Card.list_from_str(gs['deck']))
        game.heap = Heap(Card.list_from_str(gs['heap']))
        game.player_index = gs['player_index']
        game.players = [Player(data['name'], Card.list_from_str(data['hand'])) for data in gs['players']]
        game.player_size = len(game.players)
        return game

    def save(self):
        return {
            'player_index': self.player_index,
            'players': [{'name': p.name, 'hand': repr(p.hand)} for p in self.players],
            'heap': repr(self.heap),
            'deck': repr(self.deck)
        }

        # r3 r5 - Alice


# b1 g2 - Bob
# g3 - heap
# y9 - deck
# d = Deck.create_from_string('r3 r5 b1 g2 g3 y9')
# app = UnoGame(['Alice', 'Bob'], hand_size=2, deck=d)


game_state = {
    'player_index': 0,
    'players': [
        {
            'name': 'Charly',
            'hand': 'r3 r5'
        },
        {
            'name': 'Bob',
            'hand': 'b1 g2'
        },

    ],
    'heap': 'r4 g5 g3',
    'deck': 'y9 r9 y0 y1'
}

app = UnoGame.create(['Charly', 'Bob', 'Olga', 'Natasha'])
#app = UnoGame.load(game_state)
# print(app)
print(json.dumps(app.save(), indent=4))
app.run()
