'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def var_getavailableletters(var_lettersguessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    var_a = list("abcdefghijklmnopqrstuvwxyz")
    var_b = sorted(var_lettersguessed)
    var_acopy = var_a[:]
    for i in var_acopy:
        if i in var_b:
            var_a.remove(i)
    return ''.join(var_a)
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for i in secret_word:
        if i not in letters_guessed:
            secret_word = secret_word.replace(i, " _ ")
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        for i in letters_guessed:
            secret_word = secret_word.replace(i, "")
        if secret_word == "":
            return True
        return False
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) + "letters long.")
    print("\n")
    i = 8
    flag = 0
    letters_guessed = []
    while i >= 1:
        print("You have " + str(i) + "guesses left.")
        if i <= 8 and flag == 1:
            print("Available letters: " + var_getavailableletters(letters_guessed))
        if i == 8 and flag == 0:
            print("Available letters: " + var_getavailableletters([" "]))
            flag = 1
        a = input("Please guess a letter: ")
        if a not in letters_guessed:
            letters_guessed.append(a)
            if a in secretWord:
                print("Good guess: " + get_guessed_word(secretWord, letters_guessed))
            else:
                print("Oops! You've wrong guessed that letter: " + get_guessed_word(secretWord, letters_guessed))
                i -= 1
        else:
            print("You've already used that letter as a guess, try with other guess.")
        e = is_word_guessed(secretWord, letters_guessed)
        if e:
            return "Congratulations, you won!"
        if i == 0 and e == False:
            return "Sorry you ran out of guesses, the word was " + secretWord
          

def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    print(hangman(secretWord))


if __name__ == "__main__":
    main()