""""module imported to generate random number"""
import random

# Versión Orientada a Objetos (OOP)

class Game:
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer

    def start(self):
        num_to_guess = random.randint(1, 100)
        print(f"Secret number: {num_to_guess}\n")
        print("GUESS THE SECRET NUMBER\n")
        return num_to_guess
    
    def play_turn(self, secret_num):
        human_guess = self.human.make_guess()
        self.check_guess(self.human, human_guess, secret_num)
        if human_guess == secret_num:
            return True
        computer_guess = self.computer.make_guess(self.computer.hints[-1], self.computer.guesses[-1])
        self.computer.guesses.append(computer_guess)
        self.check_guess(self.computer, computer_guess, secret_num)
        if computer_guess == secret_num:
            return True
        return False
    
    def check_guess(self, player, guess, secret_num):
        if guess < secret_num:
            print("Wrong, too low!\n")
            player.hints.append("too low")
        elif guess > secret_num:
            print("Wrong, too high!\n")
            player.hints.append("too high")
        else:
            print(f"Congratulations! {guess} is the secret number :)")
            print("Attempts:", player.guesses[1::])
            print("Total attempts:", len(player.guesses) - 1)
    
    def end_game(self):
        play_again = input("\nDo you want to play again? Type 'y' or 'n' ")
        if play_again == "n":
            print("Thank you for playing :)")
            return False
        return True

class Player:
    def __init__(self):
        self.guesses = [0]
        self.hints = [""]
        self.min_num = 1
        self.max_num = 100
        
    def make_guess(self):
        pass
    
class HumanPlayer(Player):
    def make_guess(self):
        player_num = int(input("Player 1: Enter your guess: "))
        return player_num

class ComputerPlayer(Player):
    def make_guess(self, last_hint, last_guess):
        if last_hint == "too low":
            if last_guess > self.min_num:
                self.min_num = last_guess + 1
            guess = random.randint(self.min_num, self.max_num)
            print("Computer: Enter your guess: ", guess)
            return guess
        if last_hint == "too high":
            if last_guess < self.max_num:
                self.max_num = last_guess - 1
            guess = random.randint(self.min_num, self.max_num)
            print("Computer: Enter your guess: ", guess)
            return guess
        guess = random.randint(1, 100)
        print("Computer: Enter your guess: ", guess)
        return guess

if __name__ == "__main__":
    while True:
        human_player = HumanPlayer()
        computer = ComputerPlayer()
        game = Game(human_player, computer)
        secret_num = game.start()
        while True:
            did_anyone_guess = game.play_turn(secret_num)
            if did_anyone_guess is True:
                break
        again = game.end_game()
        if again is False:
            break


# ORIGINAL ------------------

# def verify(guess, secret_num, guesses, hint):
#     """compares players' guesses to the secret number"""
#     guesses.append(guess)
#     if guess < secret_num:
#         print("Wrong, too low!\n")
#         hint.append("too low")
#         return False
#     if guess > secret_num:
#         print("Wrong, too high!\n")
#         hint.append("too high")
#         return False
#     print(f"Congratulations! {guess} is the secret number :)")
#     print("Attempts:", guesses[1::])
#     print("Total attempts:", len(guesses)-1)
#     return True


# def computer_guess(last_guess, last_hint):
#     """returns a number according to the hint"""
#     if last_hint == "too low":
#         return random.randint(last_guess+1, 100)
#     if last_hint == "too high":
#         return random.randint(1, last_guess-1)
#     return random.randint(1, 100)


# if __name__ == "__main__":
#     while True:
#         num_to_guess = random.randint(1, 100)
#         print(f"Secret number: {num_to_guess}\n")
#         print("GUESS THE SECRET NUMBER\n")
#         guesses_player = [0]
#         guesses_computer = [0]
#         hints =  ["", ""]
#         while True:
#             print("----Player 1----")
#             player_num = int(input("Player 1: Enter your guess: "))
#             verify_player = verify(player_num, num_to_guess, guesses_player, hints)
#             if verify_player is True:
#                 break
#             computer_num = computer_guess(guesses_computer[-1], hints[-2])
#             print("----Computer----\nComputer: Enter your guess:", computer_num)
#             verify_computer = verify(computer_num, num_to_guess, guesses_computer, hints)
#             if verify_computer is True:
#                 break
#         play_again = input("\nDo you want to play again? Type 'y' or 'n' ")
#         if play_again == "n":
#             print("Thank you for playing :)")
#             break

