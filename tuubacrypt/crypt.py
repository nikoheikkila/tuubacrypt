"""module: tuubacrypt"""

import re

from .deck import Deck

class TuubaCrypt():
    """Class providing the methods for encryption and decryption"""

    T_PATTERN = "[A-Z0-9]+"

    def __init__(self):
        self.pattern = re.compile(self.T_PATTERN)


    def encrypt(self, text: str) -> str:
        """
        :param self
        :param text string
        :return string
        """
        if not text:
            return ""

        result = []
        i = 1

        for char in text:
            value = char

            if self.should_translate(char):
                value = self.shift_right(char, i)
                i += 1

            result.append(value)

        return "".join(result)


    def decrypt(self, text: str) -> str:
        """
        :param self
        :param text string
        :return string
        """

        if not text:
            return ""

        result = []
        i = 1

        for char in text:
            value = char

            if self.should_translate(char):
                value = self.shift_left(char, i)
                i += 1

            result.append(value)

        return "".join(result)

    def should_translate(self, char: str) -> bool:
        """
        :param self
        :param char string
        :return bool
        """

        return self.pattern.match(char)

    def shift_right(self, char: str, count: int) -> str:
        deck = Deck.create(char=char)
        deck.shift_right(deck.position(char), count)

        return deck.pop()

    def shift_left(self, char: str, count: int) -> str:
        deck = Deck.create(char=char)
        deck.shift_left(deck.position(char), count)

        return deck.pop()
