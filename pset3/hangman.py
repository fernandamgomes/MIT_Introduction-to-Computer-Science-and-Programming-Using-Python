# -----------------------------------
# HELPER CODE
import random

# If you see an IOError, you should change the value of the WORDLIST_FILENAME constant to the complete path name for the file words.txt.
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

# END OF HELPER CODE
# -----------------------------------

# Load the list of words into the variable wordlist so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
      if char not in lettersGuessed: 
        return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_printed = ""
    for char in secretWord:
      if char in lettersGuessed: 
        word_printed = word_printed + char
      else:
        word_printed = word_printed + "_ "
    return word_printed



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = string.ascii_lowercase
    alpha_available = ""
    for char in alphabet:
      if char not in lettersGuessed:
        alpha_available = alpha_available + char
    return alpha_available

print(getAvailableLetters("['e', 'i', 'k', 'p', 'r', 's']"))
    

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
    # VARIABLES
    guesses = 8
    lettersGuessed = []
    guessed = False
    # >> available letters
    # >> users_input
    # >> condition 

    # start game
    print("Welcome to the game Hangman!")
    # let user know the legth of the secret word 
    print("I am thinking of a word that is %d letters long." %len(secretWord))
    print("-------------")

    # keep repeating the same steps until you run out of guesses or you guess the word
    while (guesses != 0) and (guessed is False):
      # let user know how many guesses are left 
      print("You have %d guesses left" %guesses)
      # update available letters
      availableLetters = getAvailableLetters(lettersGuessed)
      print("Available letters:", availableLetters)
      # ask for users input, only alphabetic letters are valid
      while True:
        users_input = str(input("Please guess a letter: "))
        if users_input.isalpha() == True:
          break
        print("Invalid guess: guesses must be alphabet letters.")
      # if the letter guessed hasn't been guessed before: 
      if users_input in availableLetters:
        # update letters guessed, number of guesses stays the same
        lettersGuessed.append(users_input)
        # if guess is right, check if the word has been guessed
        if users_input in secretWord:
          print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
          print("------------")
          guessed = isWordGuessed(secretWord, lettersGuessed)
        # else if guess is wrong
        elif users_input not in secretWord:
          # update number of guesses
          guesses = guesses - 1
          print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
          print("------------")
      # else if the letter guessed has been guessed before the number of guesses remain the same, let user know guess is not valid
      else:
        print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        print("------------")
      
    # when you exit the loop the game is over either way. Check if it ended because you ran out of guesses or because the word was guessed. Print the result
    if (guessed is True):
      print("Congratulations, you won!")
    else:
      print("Sorry, you ran out of guesses. The word was", secretWord)

# testing
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
