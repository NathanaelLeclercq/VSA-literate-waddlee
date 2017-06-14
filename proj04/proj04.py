# Name: Nathanael Leclercq
# Date: June 13

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""\

mystring = raw_input("enter the word to see if it is a palindrome or not: ")


wordlist = [mystring]

#print wordlist

stringlist = []
for letter in mystring:
    stringlist.append(letter)

#print stringlist

stringlist_reverse = []

lst = stringlist
while lst:
    stringlist_reverse.append(lst[-1])
    lst = lst[:-1]

print stringlist_reverse

# if stringlist_reverse == stringlist:
#     print "This is a Palindrome"
# else:
#     print  "This is not a Palindrome"