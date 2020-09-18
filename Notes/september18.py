"""
Today we will learn about FUNCTIONS.
Functions do things for us.
They take inputs or
just do instructions, and give outputs.
"""

#some functions are made for us. Example:
import math
math.sqrt(4)

#lets make our own function.
# we need to use def as a keyword
def my_function():
    print('nice fanny pack!!!')
    print('thats a cool fanny pack')

#notice that the function didnt work yet
# we need to CALL the function.
my_function()

#let's create a function with an ARGUMENT
#an argument goes into the function brackets

def print_what_i_say(x):
    print(x) #this will print whatever is in x

x = 4

print_what_i_say(x)

#we will create a custom greeting
y = 'Jeff'
def greeting(y):
    print('Welcome,' + y + 'How are you doing today?')

greeting(y)

#lets use multiple arguments

def multiply_three(num1, num2, num3):
    #the arguments must be int/float
    x = num1*num2*num3
    print(x)

multiply_three(300642,3,0.15)

    

def right_justify(s):


