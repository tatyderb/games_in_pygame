from __future__ import annotations

import json

from uno_stepik.card import Card
from uno_stepik.card_list import Deck, Heap
from uno_stepik.player import Player


class Game:
    def __init__(self):
        self.deck = None  # колода
        self.heap = None  # отбой
        self.players = None  # игроки
        self.player_index = None  # индекс текущего игрока

    @staticmethod
    def create(name_list: list[str], cards: list[Card] | None = None) -> Game:
        """ Создает новую игру с игроками из name_list и картами cards"""
        pass

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
# game = Game.create(['Bob', 'Charley'])
# или загружаем состояние игры из game_state
game = Game.load(game_state)
print(json.dumps(game.save(), indent=4))
game.run()
