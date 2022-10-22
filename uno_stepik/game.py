from __future__ import annotations

import json


class Card:
    pass


class Deck:
    def __init__(self, cards: list[Card]):
        self.cards = cards


class Heap:
    def __init__(self, cards: list[Card]):
        self.cards = cards


class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = cards


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.hand = Hand(cards)


class Game:
    def __init__(self) -> Game:
        self.deck = None            # колода
        self.heap = None            # отбой
        self.players = None         # игроки
        self.player_index = None    # индекс текущего игрока

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

    def run(self):
        pass

    def save(self):
        pass


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
print(json.loads(game.save(), indent=4))
# game.run()
