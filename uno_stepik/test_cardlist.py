from uno_stepik.card import Card
from uno_stepik.card_list import CardList, Deck, Hand, Heap

example_card_list = [Card('red', 4), Card('blue', 5), Card('yellow', 0), Card('green', 9)]


def test_card_list():
    cl = CardList(example_card_list.copy())
    assert repr(cl) == 'r4 b5 y0 g9'
    assert len(cl) == 4

    cl.add(Card('red', 8))
    assert repr(cl) == 'r4 b5 y0 g9 r8'
    assert len(cl) == 5

    cl.add(Card('green', 1))
    assert repr(cl) == 'r4 b5 y0 g9 r8 g1'
    assert len(cl) == 6

    # Работа с пустым списком
    cl = CardList([])
    assert repr(cl) == ''
    assert len(cl) == 0

    cl.add(Card('blue', 2))
    assert repr(cl) == 'b2'
    assert len(cl) == 1


def test_heap():
    heap = Heap(example_card_list.copy())

    assert heap.top() == Card('green', 9)
    assert str(heap) == 'g9'


def test_deck():
    deck = Deck(example_card_list.copy())
    card = deck.draw()
    assert card == Card('red', 4)
    assert repr(deck) == 'b5 y0 g9'

    card = deck.draw()
    assert card == Card('blue', 5)
    assert repr(deck) == 'y0 g9'

    card = deck.draw()
    assert card == Card('yellow', 0)
    assert repr(deck) == 'g9'

    card = deck.draw()
    assert card == Card('green', 9)
    assert repr(deck) == ''


def test_hand():
    init_str = 'r3 g5 r7 y5'
    hand = Hand(Card.list_from_str(init_str))

    # можно играть всю руку
    assert repr(hand.playable_cards(Card('red', 5))) == '[r3, g5, r7, y5]'

    # можно играть по цвету
    assert repr(hand.playable_cards(Card('red', 0))) == '[r3, r7]'
    assert repr(hand.playable_cards(Card('green', 0))) == '[g5]'

    # можно играть по номеру
    assert repr(hand.playable_cards(Card('blue', 5))) == '[g5, y5]'
    assert repr(hand.playable_cards(Card('blue', 7))) == '[r7]'

    # нельзя играть ни одной
    assert repr(hand.playable_cards(Card('blue', 0))) == '[]'


def test_hand_remove_card():
    init_str = 'r3 g5 r7 y5'
    hand = Hand(Card.list_from_str(init_str))
    hand.remove(Card('green', 5))

    # можно играть всю руку
    assert repr(hand) == 'r3 r7 y5'
