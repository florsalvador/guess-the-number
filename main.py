""""module imported to generate random number"""
import random

number_guessed = False

def play(player, guess, guesses, secret_num, hint):
    """compares players' guesses to the secret number"""
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

def computer_guess(last_guess, last_hint):
    """returns a number according to the hint"""
    if last_guess == 0:
        return random.randint(1, 100)
    if last_hint == "too low":
        return random.randint(last_guess+1, 100)
    if last_hint == "too high":
        return random.randint(1, last_guess-1)

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





# Versión Orientada a Objetos (OOP)

# class Game:
#     def start(self):
#         return "x"
    
#     def play_turn(self):
#         return "x"
    
#     def check_guess(self, player_guess, secret_num, hints):
#         if player_guess < secret_num:
#             print("Wrong, too low!\n")
#             hints.append("too low")
#         elif player_guess > secret_num:
#             print("Wrong, too high!\n")
#             hints.append("too high")
#         else:
#             print(f"Congratulations! {player} guessed the number")
#             print("Attempts:", guesses[1::])
#             print("Total attempts:", len(guesses)-1)
    
#     def end_game(self):
#         return "x"
    

# class Player:
#     def __init__(self, name, guesses):
#         self.name = name
#         self.guesses = guesses

#     def make_guess(self):
#         player_num = int(input("Player 1: Enter your guess: "))
#         return player_num
    

# class ComputerPlayer(Player):
#     def make_guess(self, last_guess, last_hint):
#         if last_guess == 0:
#             return random.randint(1, 100)
#         if last_hint == "too low":
#             return random.randint(last_guess+1, 100)
#         if last_hint == "too high":
#             return random.randint(1, last_guess-1)
    

# guesses_player = []
# guesses_computer = []
# hints = []
# player = Player("Player 1", guesses_player)
# computer = Player("Computer", guesses_computer)

# num_to_guess = random.randint(1, 100)
# print(num_to_guess)

# while True:
#     print("----Player 1----")
#     Player.make_guess()
#     Game.
#     play("Player 1", player_num, guesses_player, num_to_guess, hints)
#     if number_guessed is True:
#         break
#     print("----Computer----")
#     player_num = computer_guess(guesses_computer[-1], hints[-2])
#     play("Computer", player_num, guesses_computer, num_to_guess, hints)
#     if number_guessed is True:
#         break

