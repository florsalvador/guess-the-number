import random

secretNum = random.randint(1, 100)
print(secretNum)

guessesPlayer = []
guessesComputer = []

# crear funcion para meter los ifs y los prints de player y computer

while True:
  print("----Player 1----")
  playerNum = int(input("Player 1: Enter your guess: "))
  guessesPlayer.append(playerNum)
  if playerNum != secretNum:
    if playerNum < secretNum:
      print("Too low")
    else:
      print("Too high")
    print("----Computer----")
    computerNum = random.randint(1, 100)
    guessesComputer.append(computerNum)
    print("Computer: Enter your guess:", computerNum)
    if computerNum != secretNum:
      if computerNum < secretNum:
        print("Too low")
      else:
        print("Too high")
    else:
      print("Congratulations! Computer guessed the number")
      print("Attempts:", guessesComputer)
      print("Total attempts:", len(guessesComputer))
      break
  else:
    print("Congratulations! You guessed the number")
    print("Attempts:", guessesPlayer)
    print("Total attempts:", len(guessesPlayer))
    break

# playAgain = input("Do you want to play again? Type Y or N")

# while playerNum != secretNum:


# for guess in guesses:
#   if guess != secretNum:
#     if guess < secretNum:
#       print("Too low")
#     else:
#       print("Too high")


# if playerNum != secretNum:
#   if playerNum < secretNum:
#     print("Too low")
#   else:
#     print("Too high")
#   print("----Computer----")
#   computerNum = random.randint(1, 100)
#   print("Computer: Enter your guess:", computerNum)
#   if computerNum != secretNum:
#     if computerNum < secretNum:
#       print("Too low")
#     else:
#       print("Too high")
#   else:
#     print("Congratulations! Computer guessed the number")
# else:
#   print("Congratulations! You guessed the number")
