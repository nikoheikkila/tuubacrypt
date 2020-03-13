"""module: deck.py"""

from __future__ import annotations
from string import ascii_uppercase, digits
from collections import deque
from typing import Optional

from .helpers import is_digit, is_uppercase

class DeckNotFoundException(Exception):
    pass

class Deck:
    """Represents a 'card deck' composed of items."""

    def __init__(self, string: str):
        self.queue = deque(string)

    @staticmethod
    def create(**kwargs: str) -> Deck:
        """Factory method for this class"""
        char = kwargs['char'] or ''

        if is_digit(char):
            return Deck(digits)

        if is_uppercase(char):
            return Deck(ascii_uppercase)

        raise DeckNotFoundException(f"Given character '{char}' doesn't belong to any known decks [A-Z, 0-9]")

    @classmethod
    def shift_right(cls, char: str, count: int) -> str:
        deck = cls.create(char=char)

        deck.rotate_right(deck.position(char), count)

        return deck.pop()

    @classmethod
    def shift_left(cls, char: str, count: int) -> str:
        deck = cls.create(char=char)

        deck.rotate_left(deck.position(char), count)

        return deck.pop()

    def position(self, char: str) -> int:
        return self.queue.index(char)

    def rotate_right(self, start: int = 0, step: int = 1) -> None:
        self.queue.rotate(0 - (start + step))

    def rotate_left(self, start: int = 0, step: int = 1) -> None:
        self.queue.rotate(step - start)

    def pop(self) -> str:
        return self.queue.popleft()
