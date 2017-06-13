# Name:Nathanael L
# Date: June 12


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
user_input = int(raw_input("Guess the Number the computer is thinking: "))

import random
answer = random.randint(1,9)
print user_input
print 'Your Quess'

for x in range(2):


    if user_input > answer:
        print "Too High"

    if user_input <  answer:
        print "Too Low"

    if user_input == answer:
        print " Exactly correct"

    user_input = int(raw_input("Guess the Number the computer is thinking: "))


    if user_input > answer:
        print "Too High"

    if user_input <  answer:
        print "Too Low"

    if user_input == answer:
        print " Exactly correct"

    if user_input == answer:
        print "End of Game, congratuations professional"





















































