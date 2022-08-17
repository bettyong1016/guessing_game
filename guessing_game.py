"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("-----------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("-----------------------------------")
    
    numberToBeGuessed = random.randint(1,10)
    print(numberToBeGuessed, "number to be guessed")
    count = 0
    
    while True:
        answerStr = input("Pick a number between 1 and 10: ")
        try:
            answer = int(answerStr)
            if(answer < 0 or answer >10):
                continue
            if answer <  numberToBeGuessed:
                print("It is higher!")
                count+=1
            
            elif answer > numberToBeGuessed:
                print("It is lower!")
                count+=1
            elif answer == numberToBeGuessed:
                count+=1
                print("You got it! It took you {} tries".format(count))
                break
            
        except ValueError:
            print("This is not a valid value. Please guess again.")
    end_game(count)
            
def end_game(count):
    while True:
        answer = input("Would you like to play again [y]es/[n]o: ")
        answer = answer.lower()
        if answer == 'y':
            print("The last score is {}".format(count))
            start_game()
            
        elif answer == 'n':
            print("Good bye!")
            return False
        else:
            print("Please enter a valid input! y or n")


# Kick off the program by calling the start_game function.
start_game()
