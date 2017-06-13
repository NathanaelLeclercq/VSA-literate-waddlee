# Name: Nathanael
# Date: June 12

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
user_input = raw_input("Enter your age: ")
user_input2 = raw_input("Enter your name: ")
year100 = 100 - int(user_input)
birthday = raw_input("enter Y if you had a birthday or N if you have not this year: ")
if birthday == "N":
    year100 = 99 - int(user_input)
user_input3 = raw_input(" Enter your Gender, either Male or Female:")
year2017 = 2017 + year100

if year100 < user_input:
    print
    print
    print 'you are already at least 100 years old'
print
print user_input2
print "is"
print user_input
print "years old"
print " and will be"
print year100
print 'years until you are 100 years old'
print " You will be 100 years old at year"
print year2017
print " you are the"
print user_input3
print "Gender"
