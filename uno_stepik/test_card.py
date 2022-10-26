import pytest

from uno_stepik.card import Card


def test_eq():
    # карта равна сама себе
    card1 = Card('red', 4)
    assert(card1 == card1)

    # карта равна такой же карте
    other = Card('red', 4)
    assert(card1 == other)

    # карты не равны, если цвет отличается
    assert(Card('red', 7) != Card('blue', 7))

    # карты не равны, если номер отличается
    assert(Card('blue', 2) != Card('blue', 7))

    # карты не равны, если отличается цвет и номер
    assert(Card('blue', 2) != Card('red', 7))


def test_repr():
    assert (repr(Card('blue', 2)) == 'b2')
    assert (repr(Card('red', 9)) == 'r9')
    assert (repr(Card('green', 1)) == 'g1')
    assert (repr(Card('yellow', 5)) == 'y5')


def test_create():
    assert(repr(Card.create('r2')) == 'r2')
    assert(Card.create('r2') == Card('red', 2))
    assert(Card.create('g4') == Card('green', 4))
    assert(Card.create('b0') == Card('blue', 0))
    assert(Card.create('y9') == Card('yellow', 9))


def test_list_from_str():
    assert(Card.list_from_str('r2 g4 b0 y9') == [Card('red', 2), Card('green', 4), Card('blue', 0), Card('yellow', 9)])
    assert(Card.list_from_str('r1 b4') == [Card('red', 1), Card('blue', 4)])
    assert(Card.list_from_str('g7') == [Card('green', 7)])
    assert(Card.list_from_str('') == [])


def test_validate():
    # неверный цвет
    with pytest.raises(ValueError):
        Card('pink', 5)
    # неправильное число
    with pytest.raises(ValueError):
        Card('red', 15)

    # неверный тип числа
    with pytest.raises(ValueError):
        Card('red', '5')


def test_playable():
    card = Card('red', 4)
    assert card.playable(Card('red', 4))
    assert card.playable(Card('red', 3))
    assert card.playable(Card('red', 8))
    assert card.playable(Card('blue', 4))
    assert not card.playable(Card('blue', 8))


def test_all_cards():
    cl = Card.all_cards(['red', 'blue'], [1, 3, 7])
    assert repr(cl) == '[r1, r3, r7, b1, b3, b7]'
