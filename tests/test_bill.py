"""Tests for trial.bill.split_bill (ticket #3)."""

from trial.bill import split_bill


def test_even_split():
    assert split_bill(1000, 4) == [250, 250, 250, 250]
