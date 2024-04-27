""""Module imported to generate random number"""
import random

number_guessed = False

def play(player, guess, guesses, secret_num, hint):
    """Compares players' guesses to the secret number"""
    guesses.append(guess)
    if player == "Computer":
        print("Computer: Enter your guess:", guess)
    if guess < secret_num:
        print("Wrong, too low!\n")
        hint.append("too low")
    elif guess > secret_num:
        print("Wrong, too high!\n")
        hint.append("too high")
    else:
        print(f"Congratulations! {player} guessed the number")
        print("Attempts:", guesses[1::])
        print("Total attempts:", len(guesses)-1)
        global number_guessed
        number_guessed = True

def computer_guess(guess, hint):
    """returns a number according to the hint"""
    if guess == 0:
        return random.randint(1, 100)
    if hint == "too low":
        return random.randint(guess+1, 100)
    elif hint == "too high":
        return random.randint(1, guess-1)

while True:
    num_to_guess = random.randint(1, 100)
    print(num_to_guess)
    guesses_player = [0]
    guesses_computer = [0]
    hints =  ["", ""]
    while not number_guessed:
        print("----Player 1----")
        player_num = int(input("Player 1: Enter your guess: "))
        play("Player 1", player_num, guesses_player, num_to_guess, hints)
        if number_guessed is True:
            break
        print("----Computer----")
        player_num = computer_guess(guesses_computer[-1], hints[-2])
        play("Computer", player_num, guesses_computer, num_to_guess, hints)
        if number_guessed is True:
            break
    playAgain = input("\nDo you want to play again? Type 'y' or 'n' ")
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
