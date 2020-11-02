""" Welcome to TURTLE WORLD!"""
# we can import turtle without installing things, because it
# is a native package.

import turtle

Bob = turtle.Turtle()
print(Bob)

Bob.fd(100)  # note that fd is a METHOD. This is a function on an object. 
            # we have a turtle object named bob, we are using the method
            #fd. to move him forward. 

Bob.lt(90)  #this will turn bobby 90 degrees to the left
Bob.fd(100)

# please make bob finish a square (lengths 100)
# you probably did...

Bob.fd(100)
Bob.lt(90)
Bob.fd(100)
Bob.lt(90)
Bob.fd(100)
Bob.lt(90)
Bob.fd(100)

# i could get rid of all the above, by simply doing the following:
# for this example to see better, i created Nancy the turtle 
Nancy = turtle.Turtle()

for i in range(4):
    Nancy.fd(100)
    Nancy.rt(90)

#homework. Play with for loops, try to break them (don't be scared!)








