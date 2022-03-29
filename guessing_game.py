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
    
 



  
    
  
  

   # """Psuedo-code Hints
    
  #  When the program starts, we want to:
   # ------------------------------------
  #  1. Display an intro/welcome message to the player.
  #  2. Store a random number as the answer/solution.
  #  3. Continuously prompt the player for a guess.
  #    a. If the guess greater than the solution, display to the player "It's lower".
   #   b. If the guess is less than the solution, display to the player "It's higher".
    
  #  4. Once the guess is correct, stop looping, inform the user they "Got it"
     #    and show how many attempts it took them to get the correct number.
  #  5. Let the player know the game is ending, or something that indicates the game is over.
    
#    ( You can add more features/enhancements if you'd like to. )
 #   """
  # write your code inside this function.


# Kick off the program by calling the start_game function.
