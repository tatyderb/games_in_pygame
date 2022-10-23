from uno_stepik.game import Game


def test_game_load_save():
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
    game = Game.load(game_state)
    assert(game_state == game.save())
