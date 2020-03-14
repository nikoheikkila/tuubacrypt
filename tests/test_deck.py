import pytest

from tuubacrypt.deck import Magician, Deck, DeckNotFoundException

TEST_DATA = [["A", "Z"], ["0", "9"]]


@pytest.mark.parametrize("first, last", TEST_DATA)
def test_deck_is_created(first: str, last: str):
    magician = Magician()
    deck = magician.get(first)

    assert isinstance(deck, Deck)
    assert deck.queue.pop() == last


def test_deck_raises_error_for_missing_deck():
    char = "🔥"
    magician = Magician()

    with pytest.raises(DeckNotFoundException) as e:
        assert magician.get(char=char) is None
        assert (
            str(e.message)
            == f"Given character '{char}' doesn't belong to any known decks [A-Z, 0-9]"
        )


def test_magician():
    magician = Magician()
    alphabet_round_length = 27
    digits_round_length = 11

    assert magician.left("A", alphabet_round_length) == "Z"
    assert magician.right("Z", alphabet_round_length) == "A"
    assert magician.left("0", digits_round_length) == "9"
    assert magician.right("9", digits_round_length) == "0"
