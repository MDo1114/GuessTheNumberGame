import random
import sys


def start_game():
  print("""Welcome to the Number Game!
-----------------------------
  """)
  winning_number = random.randint(1,10)
  guesses = 0
  while True:
    guessing_number = int(input("Pick a number between 1 and 10. "))
    if guessing_number == winning_number:
      guesses += 1
      print("Correct!You got it in {} guesses.".format(guesses))
      break
    elif guessing_number > winning_number:
      print("It's lower!")
      guesses += 1
    elif guessing_number < winning_number:
      print("It's higher!")
      guesses += 1

      
start_game()
play_again = input("Do you want to play again? Y/N ")
if play_again.lower() == "y":
    start_game()
else:
    sys.exit
    
 



