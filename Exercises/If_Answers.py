""" If statement answers """

# level 1-3
def tree():
    for i in range(1,8):
        print(i*'#')

#level 4-5 Beans
# Steps:
# 1 read a string (store as variable)
# 2 for each letter do this:
# 3 if a letter == "B": do this (add to a variable)

def beans():
    x = str(input('What text should we use?'))
    count = 0
    for i in x:
            if i == 'B':
                count += 1
    print('there are ', count, ' many Bs!')
            
    
#level 6-7
# if something is divisible with no remainder
# modulo (%) division will return 0

# here is the simpler way to do it...
for i in range(1,101):
    if i % 15 == 0:         # You need to have 15 first for this method to work.
        print('Fizzbuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

# the cheeky string way that was presented in class.

for i in range(1,101):
    string = ""
    if i % 3 == 0:
        string = string + "fizz"
    if i % 5 == 0:
        string = string + "buzz"
    if i % 3 != 0 and i % 5 != 0:
        string = string + str(i)
    print(string)





