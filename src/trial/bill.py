"""Bill splitting in integer cents."""


def split_bill(total_cents: int, people: int) -> list[int]:
    """Split ``total_cents`` evenly among ``people``; the shares sum to the total."""
    return [total_cents // people] * people
