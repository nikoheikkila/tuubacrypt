"""Module containing different helper scripts."""

def is_digit(char: str) -> bool:
    """Checks if a char can be converted to an integer."""
    try:
        int(char)
    except ValueError:
        return False

    return True
