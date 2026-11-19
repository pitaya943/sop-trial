"""Bill splitting in integer cents."""


def split_bill(total_cents: int, people: int) -> list[int]:
    """Split ``total_cents`` evenly among ``people``; the shares sum to the total."""
    if type(total_cents) is not int or type(people) is not int:
        raise TypeError("amounts must be integers in cents")
    if people < 1:
        raise ValueError("people must be at least 1")
    if total_cents < 0:
        raise ValueError("total_cents must not be negative")
    base, remainder = divmod(total_cents, people)
    return [base + 1 if i < remainder else base for i in range(people)]
