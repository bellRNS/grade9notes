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



