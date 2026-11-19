"""Tests for trial.bill.split_bill (ticket #3)."""

import pytest

from trial.bill import split_bill


def test_even_split():
    assert split_bill(1000, 4) == [250, 250, 250, 250]


def test_remainder_goes_one_cent_each_from_the_first_person():
    assert split_bill(1001, 3) == [334, 334, 333]


def test_shares_sum_to_total_and_differ_by_at_most_one_cent():
    for total in range(0, 250):
        for people in range(1, 12):
            shares = split_bill(total, people)
            assert len(shares) == people
            assert all(type(share) is int for share in shares)
            assert sum(shares) == total, (total, people, shares)
            assert max(shares) - min(shares) <= 1, (total, people, shares)
            assert shares == sorted(shares, reverse=True), (total, people, shares)


def test_zero_total_gives_everyone_zero():
    assert split_bill(0, 3) == [0, 0, 0]


@pytest.mark.parametrize("people", [0, -1, -5])
def test_people_below_one_is_rejected(people):
    with pytest.raises(ValueError) as excinfo:
        split_bill(1000, people)
    assert type(excinfo.value) is ValueError
    assert str(excinfo.value) == "people must be at least 1"


@pytest.mark.parametrize("total_cents", [-1, -1000])
def test_negative_total_is_rejected(total_cents):
    with pytest.raises(ValueError) as excinfo:
        split_bill(total_cents, 3)
    assert type(excinfo.value) is ValueError
    assert str(excinfo.value) == "total_cents must not be negative"


@pytest.mark.parametrize(
    ("total_cents", "people"),
    [
        (10.0, 2),
        (10.5, 2),
        (10, 2.0),
        (True, 2),
        (10, True),
        (False, 1),
        ("10", 2),
        (None, 2),
        (10, None),
    ],
)
def test_non_integer_arguments_are_rejected(total_cents, people):
    with pytest.raises(TypeError) as excinfo:
        split_bill(total_cents, people)
    assert type(excinfo.value) is TypeError
    assert str(excinfo.value) == "amounts must be integers in cents"
