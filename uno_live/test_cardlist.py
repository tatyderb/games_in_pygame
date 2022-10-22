from .card import Card
from .cardlist import Deck, Hand, Heap, CardList

from random import seed

RANDOM_SEED = 10


def test_card_list():
    """add, repr, len"""
    # __init__
    cl = CardList([Card('blue', 2), Card('blue', 4)])
    assert(repr(cl) == 'b2 b4')

    # add
    init_str = 'r3 g5 r7 y8'
    cl = CardList(Card.list_from_str(init_str))

    cl.add(Card('blue', 2))
    expected_str = init_str + ' b2'
    # print([Card('blue', 2), Card('blue', 4)])
    assert repr(cl) == expected_str

    # len
    assert len(cl) == 5


def test_heap():
    heap = Heap([Card('red', 3)])
    assert (str(heap.top()) == 'r3')
    assert (str(heap) == 'Top: r3')

    heap.add(Card('red', 7))
    assert (str(heap.top()) == 'r7')
    assert (str(heap) == 'Top: r7')

    heap.add(Card('blue', 7))
    assert (str(heap.top()) == 'b7')
    assert (str(heap) == 'Top: b7')


def test_deck():
    # d = Deck.generate(['red', 'blue'], [0, 1, 1, 2, 2])
    d = Deck(Card.list_from_str('r0 r1 r1 r2 r2 b0 b1 b1 b2 b2'))
    assert (str(d) == 'r0 r1 r1 r2 r2 b0 b1 b1 b2 b2')

    seed(RANDOM_SEED)
    d.shuffle()
    # print(d)
    assert(str(d) == 'b0 r1 b1 r1 b2 r2 r2 b1 r0 b2')


def test_deck_create():
    d = Deck([
        Card('red', 3),
        Card('green', 5),
        Card('red', 7),
        Card('yellow', 8)
    ])
    assert(str(d) == 'r3 g5 r7 y8')


def test_hand():
    init_str = 'r3 g5 r7 y8'
    hand = Hand(Card.list_from_str(init_str))

    # remove from middle
    hand.remove(Card('green', 5))
    assert str(hand) == 'r3 r7 y8'

    # remove первая
    hand.remove(Card('red', 3))
    assert str(hand) == 'r7 y8'

    # remove последняя
    hand.remove(Card('yellow', 8))
    assert str(hand) == 'r7'

    # remove единственной
    hand.remove(Card('red', 7))
    assert str(hand) == ''


def test_hand_playable():
    init_str = 'r3 g5 r7 y5'
    hand = Hand(Card.list_from_str(init_str))

    # можно играть всю руку
    assert repr(hand.playable_list(Card('red', 5))) == '[r3, g5, r7, y5]'

    # можно играть по цвету
    assert repr(hand.playable_list(Card('red', 0))) == '[r3, r7]'
    assert repr(hand.playable_list(Card('green', 0))) == '[g5]'

    # можно играть по номеру
    assert repr(hand.playable_list(Card('blue', 5))) == '[g5, y5]'
    assert repr(hand.playable_list(Card('blue', 7))) == '[r7]'

    # нельзя играть ни одной
    assert repr(hand.playable_list(Card('blue', 0))) == '[]'
