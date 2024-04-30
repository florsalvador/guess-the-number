""""module imported to generate random number"""
import random


def verify(guess, secret_num, guesses, hint):
    """compares players' guesses to the secret number"""
    guesses.append(guess)
    if guess < secret_num:
        print("Wrong, too low!\n")
        hint.append("too low")
        return False
    if guess > secret_num:
        print("Wrong, too high!\n")
        hint.append("too high")
        return False
    print(f"Congratulations! {guess} is the secret number :)")
    print("Attempts:", guesses[1::])
    print("Total attempts:", len(guesses)-1)
    return True


def computer_guess(last_guess, last_hint):
    """returns a number according to the hint"""
    if last_hint == "too low":
        return random.randint(last_guess+1, 100)
    if last_hint == "too high":
        return random.randint(1, last_guess-1)
    return random.randint(1, 100)


if __name__ == "__main__":
    while True:
        num_to_guess = random.randint(1, 100)
        print(f"Secret number: {num_to_guess}\n")
        print("GUESS THE SECRET NUMBER\n")
        guesses_player = [0]
        guesses_computer = [0]
        hints =  ["", ""]
        while True:
            print("----Player 1----")
            player_num = int(input("Player 1: Enter your guess: "))
            verify_player = verify(player_num, num_to_guess, guesses_player, hints)
            if verify_player is True:
                break
            computer_num = computer_guess(guesses_computer[-1], hints[-2])
            print("----Computer----\nComputer: Enter your guess:", computer_num)
            verify_computer = verify(computer_num, num_to_guess, guesses_computer, hints)
            if verify_computer is True:
                break
        play_again = input("\nDo you want to play again? Type 'y' or 'n' ")
        if play_again == "n":
            print("Thank you for playing :)")
            break
