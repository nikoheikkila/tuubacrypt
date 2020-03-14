import pytest

from tuubacrypt.deck import Deck, DeckNotFoundException

TEST_DATA = [
    ['A', 'Z'],
    ['0', '9']
]

@pytest.mark.parametrize("first, last", TEST_DATA)
def test_deck_is_created(first: str, last: str):
    deck = Deck.create(char=first)
    assert isinstance(deck, Deck)
    assert deck.queue.pop() == last

def test_deck_raises_error_for_missing_deck():
    char = '🔥'

    with pytest.raises(DeckNotFoundException) as e:
        assert Deck.create(char=char) is None
        assert str(e.message) == f"Given character '{char}' doesn't belong to any known decks [A-Z, 0-9]"

def test_shift():
    alphabet_round_length = 27
    digits_round_length = 11

    assert Deck.shift_left('A', alphabet_round_length) == 'Z'
    assert Deck.shift_right('Z', alphabet_round_length) == 'A'
    assert Deck.shift_left('0', digits_round_length) == '9'
    assert Deck.shift_right('9', digits_round_length) == '0'
