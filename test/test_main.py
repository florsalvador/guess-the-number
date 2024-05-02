""""functions imported from main.py"""
from main import computer_guess, verify


def test_computer_guess():
    """Testing function computer_guess(last_guess, last_hint)
    Assert 1: It should return a number higher than the guess, no more than 100.
    Assert 2: It should return a number lower than the guess, no less than 1.
    Assert 3: It should return a number lower than the guess.
    """
    assert computer_guess(99, "too low") == 100
    assert computer_guess(2, "too high") == 1
    assert computer_guess(10, "too high") < 10


def test_verify():
    """Testing function verify(guess, secret_num, guesses, hint)
    Assert 1: If the guess is equal to the secret number, then it should return True.
    Assert 2: If the guess is not equal to the secret number, then it should return False.
    """
    assert verify(20, 20, [0], ["", ""]) is True
    assert verify(15, 20, [0], ["", ""]) is False
