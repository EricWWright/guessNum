# Eric Wright & Justin Walker
# 11/18
# guessTheNumber

import random

# choices
play = ("play", "p", "start")
gPlay = ("gamble play", "g play", "g-play", "gp")
quit = ("quit", "q", "leave")

# long text vars
credits = "Credits: You either decided to play the credits first or you guessed the number correctly, but still thank you. \n this program was all able to happen because Eric Wright helped me catch up and understand the material \n Main Coder: Eric Wright Background Coder: Justin Walker"
welcome = "Welcome to Guess The Number\nIn this game you will need to guess the number the computer selects.\nYou will get 5 chances to guess the correct number. If you guess the number correctly within 5 trys then you will w"

def playGame():
  print(welcome)
  gameStart = input("Would you like to enter your own number range?")

def playGamble():
  print("Put stuff here")
  
def mainMenu():
  print("\nPlay\nGamble Play\nCredits\nQuit")
  choice = input().lower()
  if choice in play:
    print("Let's Start the game!")
    playGame()
  elif choice in gPlay:
    print("Put your money where your mouth is!")
    playGamble()
  elif choice in credits:
		print(credits)
  elif choice in quit:
    input("Press enter to quit")
  else:
    print("I don't know what you entered please try again")
    mainMenu()
mainMenu()    