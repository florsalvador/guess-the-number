""""functions imported from main.py"""
from main import computer_guess


def test_computer_guess():
    """Testing computer_guess function"""
    assert computer_guess(99, "too low") == 100



# guesses_player = [0]
# hints =  ["", ""]

# def test_verify():
#     """Testing verify function"""
#     assert verify("Player 1", 10, guesses_player, 20, hints)
