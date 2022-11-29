from __future__ import annotations

import json

from uno_stepik.card import Card
from uno_stepik.card_list import Deck, Heap
from uno_stepik.player import Player


class Game:
    class State:
        TURN_BEGIN = 'TURN_BEGIN'
        PLAY_CARD = 'PLAY_CARD'
        DRAW_CARD = 'DRAW_CARD'
        NEXT_PLAYER = 'NEXT_PLAYER'
        END = 'END'

    # сколько карт у каждого игрока в начале игры
    HAND_SIZE = 7

    def __init__(self):
        self.deck = None  # колода
        self.heap = None  # отбой
        self.players = None  # игроки
        self.player_index = None  # индекс текущего игрока
        self.state = Game.State.TURN_BEGIN

    @staticmethod
    def create(name_list: list[str], cards: list[Card] | None = None) -> Game:
        """ Создает новую игру с игроками из name_list и картами cards"""
        game = Game()

        # если карты не даны, берем всю колоду
        if cards is None:
            game.deck = Deck(Card.all_cards())
            game.deck.shuffle()
        else:
            game.deck = Deck(cards)

        print('Deck: ' + repr(game.deck))

        # создаем игроков и раздаем им по HAND_SIZE карт
        game.players = [Player(name, [game.deck.draw() for _ in range(Game.HAND_SIZE)]) for name in name_list]

        # первым ходит первый игрок
        game.player_index = 0

        # кладем первую карту отбоя
        game.heap = Heap([game.deck.draw()])

        return game

    @staticmethod
    def load(state: dict) -> Game:
        """Загружает игру из состояния state по формату:
        state = {
            'deck': 'y9 r9 y0 y1',
            'heap': 'y1 b1 b4 r4',
            'players': [
                {
                    'name': 'Bob',
                    'hand': 'r3 r5'
                },
                {
                    'name': 'Charley',
                    'hand': 'b1 g2'
                }
            ],
            'player_index': 0
        }
        """
        game = Game()
        game.deck = Deck(Card.list_from_str(state['deck']))
        game.heap = Heap(Card.list_from_str(state['heap']))
        game.players = [Player(p['name'], Card.list_from_str(p['hand'])) for p in state['players']]
        game.player_index = state['player_index']
        return game

    def save(self) -> dict:
        return {
            'deck': repr(self.deck),
            'heap': repr(self.heap),
            'player_index': self.player_index,
            'players': [p.save() for p in self.players]
        }

    def run(self):
        """ Новый run через состояния модели. """
        while self.state != Game.State.END:
            self.model_update()
        self.congratulation_winner()

    def draw_card(self):
        """ Берем карту из колоды, меняем состояние игры в зависимости от карты."""
        print('Pass! Берем карту из колоды.')
        current_player = self.current_player()
        card = self.deck.draw()
        current_player.add_card_to_hand(card)
        print(f'Взяли карту {card}')
        # * Если она подходит, её можно сразу же сыграть.
        if current_player.has_playable_card(self.heap.top()):
            self.state = Game.State.PLAY_CARD
        else:
            print(f'{current_player.name} пас')
            self.state = Game.State.NEXT_PLAYER
        print(f'{self.state=}')

    def play_card(self, card: Card = None):
        """ Играем карту card с руки в отбой, если карта None, это AI и пусть сам решает что играет."""
        if card is None:
            card = self.current_player().get_playable_card(self.heap.top())
        print(f'Play {card}')
        self.current_player().play_card(card)
        self.heap.add(card)
        print(self.current_player())
        self.state = Game.State.NEXT_PLAYER
        print(f'{self.state=}')

    def model_update(self):
        """ Подумать, надо ли что возвращать и зачем."""

        # игрок, чей сейчас ход
        current_player = self.current_player()
        # верхняя карта отбоя
        top = self.heap.top()

        # игра закончена, дальше ничего меняться не будет
        # @TODO если реализуем новую игру после окончания, менять тут
        if self.state == Game.State.END:
            return

        # следующий игрок, обрабатываем статус строго первым,
        # дальше если интерактивный игрок, то модель меняется не тут!
        if self.state == Game.State.NEXT_PLAYER:
            if len(current_player.hand) == 0:
                # текущий игрок сбросил все карты, игра закончена
                self.state = Game.State.END
            else:
                self.next_player()
                self.state = Game.State.TURN_BEGIN
            print(f'{self.state=}')
            return

        # начало хода, или играем карту, или не можем ее играть
        if self.state == Game.State.TURN_BEGIN:
            print(str(top))
            print(current_player)
            if current_player.has_playable_card(top):
                self.state = Game.State.PLAY_CARD
            else:
                self.state = Game.State.DRAW_CARD
            print(f'{self.state=}')
            return

        # надо взять карту из колоды
        if self.state == Game.State.DRAW_CARD:
            # Если подходящей карты нет, возьми карту из колоды в закрытую.
            self.draw_card()
            return

        if self.state == Game.State.PLAY_CARD:
            self.play_card()
            return

    def run_old(self):
        """Старый run через turn() """
        is_running = True
        while is_running:
            is_running = self.turn()
        self.congratulation_winner()

    def turn(self) -> bool:
        """ Возвращает False, если игра закончена. """
        # игрок, чей сейчас ход
        current_player = self.current_player()
        # верхняя карта отбоя
        top = self.heap.top()
        # Top: r4
        print(str(self.heap))
        # Bob: r3 r5
        print(current_player)
        # игрок пытается сыграть карту на отбой
        card = current_player.get_playable_card(top)
        if card is not None:
            print(f'Играет {card}')
            self.heap.add(card)
        else:
            # Если подходящей карты нет, берет карту из колоды
            print('Берет карту из колоды')
            card = self.deck.draw()
            # Если она подходит, сразу ее играет
            if card.playable(top):
                print(f'Играет {card}')
                self.heap.add(card)
            else:
                print('Пас!')
                current_player.add_card_to_hand(card)

        # после розыгрыша карт печатаем руку игрока и разделитель
        print(current_player)
        print('-'*20)

        # если все карты с руки сыграны, игра окончена
        if current_player.no_cards():
            return False

        # Ход переходит другому игроку.
        self.next_player()
        # игра продолжается
        return True

    def congratulation_winner(self):
        print(f'Поздравляем, {self.current_player().name} выиграл!')

    def current_player(self) -> Player:
        """ Текущий игрок. """
        return self.players[self.player_index]

    def next_player(self):
        """ Ход переходит к следующему игроку. """
        size = len(self.players)
        self.player_index = (self.player_index + 1) % size


'''
game_state = {
    'deck': 'y9 r9 y0 y1',
    'heap': 'y1 b1 b4 r4',
    'players': [
        {
            'name': 'Bob',
            'hand': 'r3 r5'
        },
        {
            'name': 'Charley',
            'hand': 'b1 g2'
        }
    ],
    'player_index': 0
}
# или создаем новую игру
game = Game.create(['Bob', 'Charley'])
# или загружаем состояние игры из game_state
# game = Game.load(game_state)
print(json.dumps(game.save(), indent=4))
game.run()
'''