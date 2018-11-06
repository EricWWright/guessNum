# Eric Wright & Justin Walker
# 11/18
# guessTheNumber

# imports
import random

# global vars


# choices
play = ("play", "p", "start")
gPlay = ("gamble play", "g play", "g-play", "gp")
quitG = ("quit", "q", "leave")
yes = ("yes", "y", "sure")
no = ("no", "n", "nope")
credit = ("roll credits", "play credits", "credits", "c")

# long text vars
gCredits = "Credits: You either decided to play the credits first or you guessed the number correctly, but still thank you. \n this program was all able to happen because Eric Wright helped me catch up and understand the material \n Main Coder: Eric Wright Background Coder: Justin Walker"
welcome = "Welcome to Guess The Number\nIn this game you will need to guess the number the computer selects out of a default range or a range of your choosing.\nYou will get 5 chances to guess the correct number. If you guess the number correctly within 5 trys then you will win"
welcomeG = "Welcome to Guess The Number\nIn this game you will need to guess the number the computer selects out of a default range or a range of your choosing.\nYou will also need to make a bet each time before you make a guess\nYou will be given $1000 to start betting with\nYou will get 5 chances to guess the correct number. If you guess the number correctly within 5 trys then you will win"

def playAgain():
  playAgain = input("Would you like to play again? ")
  if playAgain in yes:
    playGame()
  elif playAgain in no:
    print(gCredits)
    mainMenu()
  else:
    print("That command is not recignised please try again")
    playAgain()

def playGame():
  gameStart = input("Would you like to enter your own number range? (the default range is 1-100) (yes or no)")
  if gameStart in yes:
    numRange = input("Enter the maximum number for the range: ")
    while numRange.isalpha():
      print("Please enter a number")
      numRange = input("Enter the maximum number for the range: ")
    while numRange <= 5:
      print("The number you enter needs to be larger than 5")
      numRange = input("Enter the maximum number for the range: ")
    if numRange.isdigit():
      numRange = int(numRange)
    numToGuess = random.randint(1, numRange)
  elif gameStart in no:
    numToGuess = random.randint(1, 100)
  else:
    print("I don't know what you entered please try again")
    playGame()
  i = 0
  while i <= 6:
    guess = input("Enter a guess for what the number might be: ")
    while guess.isalpha():
      print("Please enter a number")
      guess = input("Enter a guess for what the number might be: ")
    if guess.isdigit():
      guess = int(guess)
    i = i + 1
    if guess == numToGuess:
      print("Congratulations you guessed the number correctly!")
      playAgain()
    elif guess != numToGuess and i != 5 and numToGuess > guess:
      print("I'm sorry but your guess is incorrect. Your guess was too low")
    elif guess != numToGuess and i != 5 and numToGuess < guess:
      print("I'm sorry but your guess is incorrect. Your guess was too high")
    if i == 5:
      print("I'm sorry but you loose\nThe number was", numToGuess)
      playAgain()

def playAgainG():
  playAgain = input("Would you like to play again? ")
  if playAgain in yes:
    playGamble()
  elif playAgain in no:
    print(gCredits)
    mainMenu()
  else:
    print("That command is not recignised please try again")
    playAgain()

def playGamble():
  money = 1000
  i = 0
  gameStart = input("Would you like to enter your own number range? (the default range is 1-100) ")
  if gameStart in yes:
    numRange = input("Enter the maximum number for the range: ")
    while numRange.isalpha():
      print("Please enter a number")
      numRange = input("Enter the maximum number for the range: ")
    while numRange <= 5:
      print("The number you enter needs to be larger than 5")
      numRange = input("Enter the maximum number for the range: ")
    if numRange.isdigit():
      numRange = int(numRange)
    numToGuess = random.randint(1, numRange)
  elif gameStart in no:
    numToGuess = random.randint(1, 100)
  else:
    print("I don't know what you entered please try again")
    playGamble()
  while i <= 6:
    bet = input("Make a bet: $")
    while bet.isalpha():
      print("Please enter a number")
      bet = input("Make a bet: $")
    if bet.isdigit():
      bet = int(bet)
    while bet < 50:
      print("The minimum amount you can bet is $50")
      bet = input("Make a bet: $")
      while bet.isalpha():
        print("Please enter a number")
        bet = input("Make a bet: $")
      if bet.isdigit():
        bet = int(bet)
    while bet > 1000:
      print("The maximum amount you can bet is $1000")
      bet = input("Make a bet: $")
      while bet.isalpha():
        print("Please enter a number")
        bet = input("Make a bet: $")
      if bet.isdigit():
        bet = int(bet)
    if bet > money:
      print("You don't have enough money to make that bet\n you have $", money)
      bet = input("Make a bet: $")
      while bet.isalpha():
        print("Please enter a number")
        bet = input("Make a bet: $")
      if bet.isdigit():
        bet = int(bet)
    if money < 50:
      print("You don't have enough money to keep playing")
      playAgainG()
    guess = input("Enter a guess for what the number might be: ")
    while guess.isalpha():
      print("Please enter a number")
      guess = input("Enter a guess for what the number might be: ")
    if guess.isdigit():
      guess = int(bet)
    i = i + 1
    if guess == numToGuess and i == 1:
      money = money + (bet * 3)
      print("Congradulations you guessed the number correctly the first time!\nYou walk away with $", money)
      playAgainG()
    elif guess == numToGuess and i == 2:
      money = money + (bet * 2)
      print("Congradulations you guessed the number correctly the second time!\nYou walk away with $", money)
      playAgainG()
    elif guess == numToGuess and i == 3:
      money = money + (bet * 1.5)
      print("Congradulations you guessed the number correctly the third time!\nYou walk away with $", money)
      playAgainG()
    elif guess == numToGuess and i == 4:
      money = money + (bet * 1.25)
      print("Congradulations you guessed the number correctly the fourth time!\nYou walk away with $", money)
    elif guess == numToGuess and i == 5:
      money = money + (bet * 1.125)
      print("Congradulations you guessed the number correctly the fith time!\nYou walk away with $", money)
    elif guess != numToGuess and i != 5 and numToGuess > guess:
      print("I'm sorry but your guess is incorrect. Your guess was too low")
      money = bet - money
      print("You lost $", bet)
      print("You now only have $", money)
    elif guess != numToGuess and i != 5 and numToGuess < guess:
      print("I'm sorry but your guess is incorrect. Your guess was too high")
      money = bet - money
      print("You lost $", bet)
      print("You now only have $", money)
    if i == 5 and guess != numToGuess:
      print("I'm sorry but you loose\nThe number was", numToGuess,"\nYou walk away with", money)
      playAgainG()
  
def mainMenu():
  print("\nPlay\nGamble Play\nCredits\nQuit")
  choice = input().lower()
  if choice in play:
    print("Let's Start the game!")
    print(welcome)
    playGame()
  elif choice in gPlay:
    print("Put your money where your mouth is!")
    print(welcomeG)
    playGamble()
  elif choice in credit:
    print(gCredits)
  elif choice in quitG:
    print("Bye")
  else:
    print("I don't know what you entered please try again")
    mainMenu()
mainMenu()