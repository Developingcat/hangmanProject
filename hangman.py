"""
HANGMAN 
Author: Hannah O'Shea
Date: 12/04/2024
Based on: Al Sweigart's Hangman from The Big Book of Small Python Projects 
"""

# Imports 

import random, sys

# ASCII Graphics 

HANGMAN_PICS = [r"""
    +--+
    |  |
    |  ^
    |
    |
    |
    |
    =====""",

    r"""
     +--+
    |  |
    |  ^
    |  O
    |
    |
    |
    =====""",
 r"""
     +--+
    |  |
    |  ^
    |  O
    |  |
    |
    |
    =====""",
r"""
     +--+
    |  |
    |  ^
    |  O
    | /|
    |
    |
    =====""",
r"""
     +--+
    |  |
    |  ^
    |  O
    | /|\
    |
    |
    =====""",
r"""
     +--+
    |  |
    |  ^
    |  O
    | /|\
    | /
    |
    =====""",
r"""
     +--+
    |  |
    |  ^
    |  O
    | /|\
    | / \
    |
    ====="""
]



# Categories & Words section 

CATEGORY = 'Animals' 


WORDS = 'ANT BADGER BEAVER DONKEY EAGLE GOOSE LIZARD MONKEY MOUSE PARROT PYTHON RABBIT OTTER TURTLE WEASEL WOMBAT SHARK'.split()  


# Main Program Function 

def main():
    print("Hangman, by Hannah O'Shea")
    print("==========================\n\n")
    print("based on Al Sweigart's Big Book of Small Python Projects\n\n")

    # Setup Variable for a new game: 

    missedLetters = [] # List of incorrect letter guesses. 
    correctLetters = [] # List of correct letter guesses.
    secretWord = random.choice(WORDS)



# Draw current state of the hangman game, along with the missed and correctly guessed letters of the secret word. 

def drawHangman(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(misssedLetters)])
    print('The category selected is: ', CATEGORY)
    print()


    # Show the incorrectly guessed letters 



    # Display the blanks for the secret word (one blank per letter)
blanks = ['_'] * len(secretWord)
    # Replace blanks with correctly guessed letters:

    #Show the secret word with spaces in between each letter 

# Returns the letter the player entered, this function makes sure the player entered a single letter that they haven't guessed before. 

# If this program was run (instead of imported), run the game 

if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt: 
        sys.exit() # When Ctrl-C is pressed, end game  


