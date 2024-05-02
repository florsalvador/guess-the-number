""""module imported to generate random number"""
import random

# Versión Orientada a Objetos (OOP)

class Game:
    def __init__(self, player, computer, hints):
        self.player = player
        self.computer = computer
        self.hints = hints

    def start(self):
        num_to_guess = random.randint(1, 100)
        print(f"Secret number: {num_to_guess}\n")
        print("GUESS THE SECRET NUMBER\n")
        return num_to_guess
    
    def play_turn(self, secret_num):
        player_guess = self.player.make_guess()
        self.player.guesses.append(player_guess)
        self.check_guess(player_guess, secret_num)
        if player_guess == secret_num:
            return True
        computer_guess = self.computer.make_guess(self.hints[-1], player_guess)
        self.computer.guesses.append(computer_guess)
        self.check_guess(computer_guess, secret_num)
        if computer_guess == secret_num:
            return True
        return False
    
    def check_guess(self, guess, secret_num):
        if guess < secret_num:
            print("Wrong, too low!\n")
            self.hints.append("too low")
        elif guess > secret_num:
            print("Wrong, too high!\n")
            self.hints.append("too high")
        else:
            print(f"Congratulations! {guess} is the secret number :)")
            print("Attempts:", self.player.guesses)
            print("Total attempts:", len(self.player.guesses))
    
    def end_game(self):
        play_again = input("\nDo you want to play again? Type 'y' or 'n' ")
        if play_again == "n":
            print("Thank you for playing :)")
            return False
        return True

class Player:
    def __init__(self, name, guesses, min_num, max_num):
        self.name = name
        self.guesses = guesses
        self.min_num = min_num
        self.max_num = max_num

    def make_guess(self):
        player_num = int(input(f"{self.name}: Enter your guess: "))
        return player_num

class ComputerPlayer(Player):
    def make_guess(self, last_hint, last_guess):
        if last_hint == "too low":
            self.min_num = last_guess + 1
            return random.randint(self.min_num, 100)
        if last_hint == "too high":
            self.max_num = last_guess - 1
            return random.randint(1, self.max_num)
        return random.randint(1, 100)

if __name__ == "__main__":
    while True:
        guesses = []
        hints = []
        player = Player("Player 1", guesses, 1, 100)
        computer = ComputerPlayer("Computer", guesses, 1, 100)
        game = Game(player, computer, hints)
        secret_num = game.start()
        while True:
            did_anyone_guess = game.play_turn(secret_num)
            if did_anyone_guess is True:
                break
        again = game.end_game()
        if again is False:
            break


# INTENTO -------------------------------

# class Game:
#     def __init__(self, player, computer):
#         self.player = player
#         self.computer = computer

#     def start(self):
#         num_to_guess = random.randint(1, 100)
#         print(f"Secret number: {num_to_guess}\n")
#         print("GUESS THE SECRET NUMBER\n")
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
#         play_again = input("\nDo you want to play again? Type 'y' or 'n' ")
#         if play_again == "n":
#             print("Thank you for playing :)")
    

# class Player:
#     def __init__(self, name, guesses):
#         self.name = name
#         self.guesses = guesses

#     def make_guess(self):
#         player_num = int(input("Player 1: Enter your guess: "))
#         return player_num
    

# class ComputerPlayer(Player):
#     def __init__(self, hints):
#         self.hints = hints

#     def make_guess(self):
#         if self.guesses[-1] == 0:
#             return random.randint(1, 100)
#         if self.hints[] == "too low":
#             return random.randint(last_guess+1, 100)
#         if last_hint == "too high":
#             return random.randint(1, last_guess-1)
    
# if __name__ == "__main__":
#     guesses_player = []
#     guesses_computer = []
#     hints = []
#     player = Player("Player 1", guesses_player)
#     computer = Player("Computer", guesses_computer)

#     num_to_guess = random.randint(1, 100)
#     print(num_to_guess)

#     while True:
#         print("----Player 1----")
#         Player.make_guess()
#         Game.
#         play("Player 1", player_num, guesses_player, num_to_guess, hints)
#         if number_guessed is True:
#             break
#         print("----Computer----")
#         player_num = computer_guess(guesses_computer[-1], hints[-2])
#         play("Computer", player_num, guesses_computer, num_to_guess, hints)
#         if number_guessed is True:
#             break

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

