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
    assert (t1 == t2 and t2 == t1)

    c = Card('red', 7)
    assert (t1 != c and c != t1)


def test_list_from_str():
    s = 'y6 r3 g2 b0 b5'
    expected_list = [
        Card('yellow', 6),
        Card('red', 3),
        Card('green', 2),
        Card('blue', 0),
        Card('blue', 5)
    ]
    card_list = Card.list_from_str(s)
    assert (card_list == expected_list)
