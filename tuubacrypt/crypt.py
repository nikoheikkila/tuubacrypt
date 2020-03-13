"""module: tuubacrypt"""

import re

from typing import Callable
from .deck import Deck

Shiftable = Callable[[str, int], str]

class TuubaCrypt():
    """Class providing the methods for encryption and decryption"""

    T_PATTERN = "[A-Z0-9]+"

    def __init__(self) -> None:
        self.pattern = re.compile(self.T_PATTERN)

    def encrypt(self, text: str) -> str:
        self.text = text

        return self.translate(Deck.shift_right)


    def decrypt(self, text: str) -> str:
        self.text = text

        return self.translate(Deck.shift_left)

    def translate(self, shift: Shiftable) -> str:
        if not self.text:
            return ""

        result = []
        i = 1

        for char in self.text:
            if not self.should_translate(char):
                result.append(char)
                continue

            result.append(shift(char, i))
            i += 1

        return "".join(result)

    def should_translate(self, char: str) -> bool:
        return self.pattern.match(char) is not None
