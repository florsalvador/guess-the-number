import random

numToGuess = random.randint(1, 100)
print(numToGuess)

guessesPlayer = []
guessesComputer = []

def randonNum():
  return random.randint(1, 100)

numberGuessed = False

def play(player, guesses, secretNum):
  print(f"----{player}----")
  playerNum = int(input("Player 1: Enter your guess: ")) if player == "Player 1" else randonNum()
  guesses.append(playerNum)
  if player == "Computer":
    print("Computer: Enter your guess:", playerNum)
  if playerNum < secretNum:
    print("Wrong, too low!\n")
  elif playerNum > secretNum:
    print("Wrong, too high!\n")
  else:
    print(f"Congratulations! {player} guessed the number")
    print("Attempts:", guesses)
    print("Total attempts:", len(guesses))
    global numberGuessed 
    numberGuessed = True

while not numberGuessed:
  play("Player 1", guessesPlayer, numToGuess) # por que si cambia numberGuessed a True, el bucle no se rompe aqui?
  if numberGuessed == True:
    break
  else:
    play("Computer", guessesComputer, numToGuess)



  # print("----Player 1----")
  # playerNum = int(input("Player 1: Enter your guess: "))
  # guessesPlayer.append(playerNum)
  # if playerNum != numToGuess:
  #   if playerNum < numToGuess:
  #     print("Too low\n")
  #   else:
  #     print("Too high\n")
  #   print("----Computer----")
  #   computerNum = random.randint(1, 100)
  #   guessesComputer.append(computerNum)
  #   print("Computer: Enter your guess:", computerNum)
  #   if computerNum != numToGuess:
  #     if computerNum < numToGuess:
  #       print("Too low\n")
  #     else:
  #       print("Too high\n")
  #   else:
  #     print("Congratulations! Computer guessed the number")
  #     print("Attempts:", guessesComputer)
  #     print("Total attempts:", len(guessesComputer))
  #     break
  # else:
  #   print("Congratulations! You guessed the number")
  #   print("Attempts:", guessesPlayer)
  #   print("Total attempts:", len(guessesPlayer))
  #   break

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
