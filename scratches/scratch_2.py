def myfunction():
    print "I called My function"

myfunction()


def largest(x,y):
    ans = x
    if y > x:
        return ans


largenum = largest(2,5)
print largenum



def getnum(prompt):
    ans = int(raw_input(prompt))



age = getnum("what is you age?")

grade = getnum("what is your grade?")



