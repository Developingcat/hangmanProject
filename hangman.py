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
    print("\n\nHangman, by Hannah O'Shea")
    print("==========================\n\n")
    print("based on Al Sweigart's Big Book of Small Python Projects\n\n")

    # Setup Variable for a new game: 

    missedLetters = [] # List of incorrect letter guesses. 
    correctLetters = [] # List of correct letter guesses.
    secretWord = random.choice(WORDS)

    while True: 
        drawHangman(missedLetters, correctLetters, secretWord)

        # Let the player enter their letter guess: 
        guess = getPlayerGuess(missedLetters + correctLetters) 

        if guess in secretWord: 
            # Add the correct guess to correctedLetters 
            correctLetters.append(guess) 
        
        # Check if the player has won 
        foundAllLetters = True # Start off assuming they've won, for 
        for secretWordLetter in secretWord: 
            if secretWordLetter not in correctLetters: 
                # There's a letter in the secret word that isn't yet in correctLetters, so the player hasn't won the game yet.
                foundAllLetters = False
                break
            if foundAllLetters: 
                print("Yes! The secret word is:", secretWord)
                print("You have won.")
                break # break out of the main gameloop 
        else: 
            # The player has guessed incorrectly:
            missedLetters.append(guess)
        # check if player has guessed too many times and lost, the "-1" is because we don't count the empty gallows in HANGMAN_PICS 
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            drawHangman(missedLetters, correctLetters, secretWord)
            print("You have run out of guesses.")
            print('The word was "{}"'.format(secretWord))
            break
# Draw current state of the hangman game, along with the missed and correctly guessed letters of the secret word. 

def drawHangman(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category selected is: ', CATEGORY)
    print()


    # Show the incorrectly guessed letters 
    print('Missed Letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print("No missed letters yet.")
    print()
    

    # Display the blanks for the secret word (one blank per letter)
    blanks = ['_'] * len(secretWord)
    # Replace blanks with correctly guessed letters:

    #Show the secret word with spaces in between each letter 

    # Returns the letter the player entered, this function makes sure the player entered a single letter that they haven't guessed before. 

def getPlayerGuess(alreadyGuessed): 
    while True: # This will keep asking until the player enters a valid letter. 
        print("Guess a letter:  ")
        guess = input('> ').upper()
        if len(guess) != 1: 
            print("Please enter a single letter.") 
        elif guess in alreadyGuessed:
            print("You have already guessed that letter, please guess again.") 
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        else: 
            return guess 
    


# If this program was run (instead of imported), run the game 

if __name__ == '__main__': 
    try:
        main()
    except KeyboardInterrupt: 
        sys.exit() # When Ctrl-C is pressed, end game  


