"""module: tuubacrypt"""

import re

from .deck import Magician, Shiftable


class TuubaCrypt:
    """Class providing the methods for encryption and decryption"""

    T_PATTERN = "^[A-Z0-9]$"

    def __init__(self) -> None:
        self.magician = Magician()
        self.pattern = re.compile(self.T_PATTERN)

    def encrypt(self, text: str) -> str:
        return self.translate(text, self.magician.right)

    def decrypt(self, text: str) -> str:
        return self.translate(text, self.magician.left)

    def translate(self, text: str, shift: Shiftable) -> str:
        if not text:
            return ""

        result = []
        i = 1

        for char in text:
            if not self.should_translate(char):
                result.append(char)
                continue

            result.append(shift(char, i))
            i += 1

        return "".join(result)

    def should_translate(self, char: str) -> bool:
        return self.pattern.match(char) is not None
