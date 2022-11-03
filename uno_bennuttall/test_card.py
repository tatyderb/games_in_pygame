from .card import Card


def test_create():
    c = Card('red', 3)
    assert (str(c) == '3r')

    c = Card('blue', 0)
    assert (str(c) == '0b')


def test_playable():
    top = Card('red', 3)
    good = Card('red', 3)
    assert (top.playable(good))
    good = Card('red', 7)
    assert (top.playable(good))
    good = Card('red', 1)
    assert (top.playable(good))
    good = Card('green', 3)
    assert (top.playable(good))
    good = Card('blue', 3)
    assert (top.playable(good))
    good = Card('yellow', 3)
    assert (top.playable(good))

    wrong = Card('green', 1)
    assert (not top.playable(wrong))
