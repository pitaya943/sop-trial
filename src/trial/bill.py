"""Bill splitting in integer cents."""


def split_bill(total_cents: int, people: int) -> list[int]:
    """Split a bill evenly among people, in integer cents.

    Each person gets ``total_cents // people`` cents; the leftover cents go one
    each to the first people, so the shares always sum to ``total_cents`` and
    no two shares differ by more than one cent.

    Args:
        total_cents: The bill amount in cents. Must be a non-negative ``int``.
        people: How many people share the bill. Must be an ``int`` of at least 1.

    Returns:
        A list of ``people`` shares in cents, largest first.

    Raises:
        TypeError: If either argument is not an ``int`` (``bool`` and ``float``
            are rejected).
        ValueError: If ``people`` is less than 1 or ``total_cents`` is negative.
    """
    if type(total_cents) is not int or type(people) is not int:
        raise TypeError("amounts must be integers in cents")
    if people < 1:
        raise ValueError("people must be at least 1")
    if total_cents < 0:
        raise ValueError("total_cents must not be negative")
    base, remainder = divmod(total_cents, people)
    return [base + 1 if index < remainder else base for index in range(people)]
