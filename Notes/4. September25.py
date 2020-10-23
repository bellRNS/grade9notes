"""" Generalizing some functions """
import turtle

doug = turtle.Turtle()
david = turtle.Turtle()

def square(t):
    for i in range(4):      # i generalized it to take any turtle!!!
        t.fd(100)
        t.rt(90)

        
def square_custom(t, l):   # we added a argument for length
    for i in range(4):
        t.fd(l)
        t.rt(90)

def any_polygon(t, l, n):
    x = 360 / n         #we are finding the interior angles for any shape
    for i in range(n):
        t.fd(l)
        t.rt(x)
