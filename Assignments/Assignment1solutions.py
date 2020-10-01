#remember the toast continuum (be simple but complete)

#Solution A for question 1 
def right_justify(s):
    x = len(s)
    y = 70
    z = 70-x
    print(" "*z + s)
    #i wrote all of this below, before starting to program:
        #first is to figure out the length of s is.
        #i want to set a variable to 70
        #new variable is equal to 70-s
        #print out variable spaces (________) and add s (the argument)

#Solution B for question 1 
def quick_right_justify(s):       
    print(" "*(70-len(s)) + s) #this does it all in one line.
                               #Which solution do you like more?








#Solution A for question 2: 
def print_square():
    corners = "+ - - - - + - - - - +"
    middle =  "|         |         |"
    print(corners + "\n" +          # here i am using a linebreak string \n
          (middle + "\n")*3 +       # multiplying the middle row by 3
          corners + "\n" +
          (middle + "\n")*3 +
          corners + "\n")

#Solution B for question 2:
def fast_square():
    corners = "+ - - - - + - - - - + \n" #the line break is included in variable 
    middle =  "|         |         | \n"
    print(corners + middle*3 + corners + middle*3 + corners)
                                        #Which solution do you like more?
    
