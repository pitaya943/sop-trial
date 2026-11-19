"""Bill splitting in integer cents."""


def split_bill(total_cents: int, people: int) -> list[int]:
    """Split ``total_cents`` evenly among ``people``; the shares sum to the total."""
    base, remainder = divmod(total_cents, people)
    return [base + 1 if i < remainder else base for i in range(people)]
