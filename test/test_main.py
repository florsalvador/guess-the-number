""""functions imported from main.py"""
from main import computer_guess, verify


def test_computer_guess():
    """Testing function computer_guess(last_guess, last_hint)"""
    assert computer_guess(99, "too low") == 100
    assert computer_guess(2, "too high") == 1
    assert computer_guess(10, "too high") < 10


def test_verify():
    """Testing function verify(guess, secret_num, guesses, hint)"""
    assert verify(20, 20, [0], ["", ""]) is True
    assert verify(15, 20, [0], ["", ""]) is False