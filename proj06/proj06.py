# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

wordList = load_words()
lissst = []
wordList = lissst
blue = lissst

def hangman():
    worldd = choose_word(wordlist)
    for letter in worldd:
        lissst.append(letter)
    print lissst
    user_input = str(raw_input("Guess a letter in the word: " ))
    if user_input in lissst:
        print "Correct"
    else:
        print "InCorrect"












            # while lissst:
    #     if blue[0] == lissst[0]:
    #         blue = lissst[1:-1]





















hangman()