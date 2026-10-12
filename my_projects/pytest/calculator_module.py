"""A simple calculator for my projects."""

def increment_by_one(number_to_increment: int) -> int:
    """Increments value by 1.

    Args:
        number_to_increment: Number to be incremented.

    Returns:
        Incremented value.
    """
    if not type(number_to_increment) == int:
        raise TypeError("Input must be an integer.")
    return number_to_increment + 1

def decrement_by_one(number_to_decrement: int) -> int:
    """Decrements value by 1.

    Args:
        number_to_decrement: Number to be decremented.

    Returns:
        Decremented value.
    """
    if not type(number_to_decrement) == int:
        raise TypeError("Input must be an integer.")
    return number_to_decrement - 1