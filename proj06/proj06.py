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

alpha = []
lissst = []
wordList = lissst
boop2 = []
def hangman():
    worldd = choose_word(wordlist)
    for letter in worldd:
        lissst.append(letter)

    print lissst
    lissst2 = []


    lissst2 = ('_ ' * len(lissst))


    print lissst2,
    number_guesses = 8
    while number_guesses > 0:
        print lissst2
        print "your guesses:", boop2
        if number_guesses > 0:
            user_input = str(raw_input("Guess a letter in the word: "))
            for boop in user_input:
                boop2.append(boop)
            if user_input in lissst:

                print "Correct"
            else:
                number_guesses -= 1
                print "InCorrect", number_guesses, "Guesses left"
        if  boop2== lissst:
            print "YOU WIN!"
            break

        if number_guesses == 0:
            print "GAME OVER!!!"
            break







                # while lissst:
        #     if blue[0] == lissst[0]:
        #         blue = lissst[1:-1]


hangman()