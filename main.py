""""Module imported to generate random number"""
import random

def random_num():
    """Returns a random number between 1 and 100"""
    return random.randint(1, 100)

number_guessed = False

def play(player, guesses, secret_num):
    """Compares players' guesses to the secret number"""
    print(f"----{player}----")
    player_num = (
        int(input("Player 1: Enter your guess: "))
        if player == "Player 1"
        else random_num()
    )
    guesses.append(player_num)
    if player == "Computer":
        print("Computer: Enter your guess:", player_num)
    if player_num < secret_num:
        print("Wrong, too low!\n")
    elif player_num > secret_num:
        print("Wrong, too high!\n")
    else:
        print(f"Congratulations! {player} guessed the number")
        print("Attempts:", guesses)
        print("Total attempts:", len(guesses))
        global number_guessed
        number_guessed = True

while True:
    num_to_guess = random_num()
    print(num_to_guess)
    guesses_player = []
    guesses_computer = []
    while not number_guessed:
        play("Player 1", guesses_player, num_to_guess)
        if number_guessed is True:
            break
        play("Computer", guesses_computer, num_to_guess)
        if number_guessed is True:
            break
    playAgain = input("\nDo you want to play again? Type y for yes ")
    if playAgain == "y":
        number_guessed = False
    else:
        print("Thank you for playing :)")
        break


# por que si cambia numberGuessed a True, el bucle no se rompe aqui?
# while not number_guessed:
#     play("Player 1", guesses_player, num_to_guess)
#     if number_guessed is True:
#         break
#     play("Computer", guesses_computer, num_to_guess)
