"""Tests for trial.bill.split_bill (ticket #3)."""

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
