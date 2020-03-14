"""module: deck.py"""

from __future__ import annotations
from typing import Callable
from string import ascii_uppercase, digits
from collections import deque

from .helpers import is_digit, is_uppercase

Shiftable = Callable[[str, int], str]


class DeckNotFoundException(Exception):
    pass


class Magician:
    def __init__(self) -> None:
        self.decks = {"upper": Deck(ascii_uppercase), "digits": Deck(digits)}

    def get(self, char: str) -> Deck:
        if is_uppercase(char):
            return self.decks["upper"]

        if is_digit(char):
            return self.decks["digits"]

        raise DeckNotFoundException(
            f"Given character '{char}' doesn't belong to any known decks [A-Z, 0-9]"
        )

    def left(self, char: str, count: int) -> str:
        deck = self.get(char)
        deck.rotate_left(deck.position(char), count)

        return deck.first()

    def right(self, char: str, count: int) -> str:
        deck = self.get(char)
        deck.rotate_right(deck.position(char), count)

        return deck.first()


class Deck:
    """Represents a 'card deck' composed of items."""

    def __init__(self, string: str):
        self.queue = deque(string)

    def position(self, char: str) -> int:
        return self.queue.index(char)

    def rotate_right(self, start: int = 0, step: int = 1) -> None:
        self.queue.rotate(0 - (start + step))

    def rotate_left(self, start: int = 0, step: int = 1) -> None:
        self.queue.rotate(step - start)

    def first(self) -> str:
        return self.queue[0]
