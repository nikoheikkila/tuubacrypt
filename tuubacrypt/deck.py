"""module: deck.py"""

from __future__ import annotations
from string import ascii_uppercase, digits
from collections import deque

from .helpers import is_digit


class Deck:
    """Represents a 'card deck' composed of items."""

    @staticmethod
    def create(**kwargs) -> Deck:
        """Factory method for this class"""
        if is_digit(kwargs['char']):
            return Deck(digits)

        return Deck(ascii_uppercase)

    def __init__(self, string: str):
        self.queue = deque(string)

    def position(self, char: str) -> int:
        """
        Returns the position of a character in alphabet
        or None if there's no match.
        """
        try:
            return self.queue.index(char)
        except ValueError:
            return None

    def shift_right(self, start: int = 0, step: int = 1):
        self.queue.rotate(-(start + step))

    def shift_left(self, start: int = 0, step: int = 1):
        self.queue.rotate(step - start)

    def pop(self):
        return self.queue.popleft()
