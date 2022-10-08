from .card import Card


def test_create_print():
    c = Card('red', 3)
    # print(c)
    assert (str(c) == 'r3')


def test_playable():
    t = Card('red', 3)

    c = Card('red', 7)
    assert c.playable(t)

    c = Card('red', 0)
    assert c.playable(t)

    c = Card('red', 3)
    assert c.playable(t)

    c = Card('green', 3)
    assert c.playable(t)

    c = Card('blue', 3)
    assert c.playable(t)

    c = Card('yellow', 3)
    assert c.playable(t)

    c = Card('green', 6)
    assert not c.playable(t)

    c = Card('green', 2)
    assert not c.playable(t)


def test_eq():

    t1 = Card('red', 3)
    t2 = Card('red', 3)
    assert(t1 == t2 and t2 == t1)

    c = Card('red', 7)
    assert(t1 != c and c != t1)

