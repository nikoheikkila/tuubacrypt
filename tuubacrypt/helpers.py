"""Module containing different helper scripts."""

ORDERS = {'A': 65, 'Z': 90}

def is_digit(char: str) -> bool:
    """Checks if a char can be converted to an integer."""
    try:
        int(char)
    except ValueError:
        return False

    return True

def is_uppercase(char: str) -> bool:
    return ord(char) in range(ORDERS['A'], ORDERS['Z'] + 1)
