import turtle 

#### Level 1 

t = turtle.Turtle()

def square(t,l):
    #t and l are turtle and length
    for i in range(4):
        t.fd(l)
        t.rt(90)

#### Level 2 

def multi_squares(t,n):
    #t and n are turtle and number of squares drawn
    for i in range(4*n):
        square(t,100)

def fancy_multi(t,n):
    for i in range(n):
        square(t,100)
        t.pendown()
        t.fd(15)


#### Level 3 

def any_shape(t,s):
    #t and s are turtle and side number, x is interior angle length
    x = 360/s
    for i in range(s):
        t.fd(50)
        t.rt(x)


#### Level 4 & 5 

#I'm going to create some functions for common keystrokes

def back(t,l):
    # t is turtle and l is length
    t.rt(180)
    t.fd(l)

def line(t,l,head):
    # t is turtle and l is length
    # head is orientation on page (360 degrees total)
    t.setheading(head)
    t.fd(l)


# starting my alphabet 
    
def letter_a(t):
    line(t,100,70)
    line(t,100,290)
    back(t,50)
    line(t,40,180)

def letter_b(t):
    line(t,100, 90)
    line(t,40, 0)
    line(t,50, 270)
    line(t,40,180)
    back(t,60)
    line(t, 50, 270)
    line(t, 60, 180)

def letter_c(t):
    line(t, 100, 90)
    line(t, 50, 0)
    back(t,50)
    line(t, 100, 270)
    line(t, 50, 0)

def letter_d(t):
    line(t, 100, 90)
    line(t, 50, 0)
    line(t, 10, 315)
    line(t, 84, 270)
    line(t, 10, 225)
    line(t, 50, 180)

def letter_e(t):
    line(t, 100, 90)
    line(t, 50, 0)
    back(t, 50)
    line(t, 50, 270)
    line(t, 35, 0)
    back(t, 35)
    line(t, 50, 270)
    line(t, 50,0)

def letter_f(t):
    line(t, 100, 90)
    line(t, 50, 0)
    back(t, 50)
    line(t, 50, 270)
    line(t, 35, 0)
    back(t, 35)
    line(t, 50, 270)

def letter_g(t):
    line(t, 100, 90)
    line(t, 50, 0)
    back(t, 50)
    line(t, 100, 270)
    line(t, 50, 0)
    line(t, 50, 90)
    line(t, 25, 180)

def letter_h(t):
    line(t, 100, 90)
    back(t, 50)
    line(t, 40, 0)
    line(t, 50, 90)
    back(t,100)

def letter_i(t):
    line(t, 50, 0)
    back(t, 25)
    line(t, 100, 90)
    line(t, 25, 180)
    back(t, 50)

def letter_j(t):
    line(t, 50, 0)
    line(t, 100, 90)
    line(t, 50, 180)
    back(t, 100)

def letter_k(t):
    line(t, 100, 90)
    back(t, 35)
    line(t, 35, 45)
    back(t, 35)
    line(t, 90, 315)

def letter_l(t):
    line(t, 100, 90)
    back(t, 90)
    line(t, 70, 0)

def letter_m(t):
    line(t,100,90)
    line(t,100,300)
    line(t,100,60)
    line(t,100,270)

def letter_n(t):
    line(t,100,90)
    line(t,120,300)
    line(t,100, 90)

def letter_o(t):
    line(t,100,90)
    line(t,50,0)
    line(t,100,270)
    line(t,50,180)

def letter_p(t):
    line(t,100, 90)
    line(t,50,0)
    line(t, 50, 270)
    line(t,50, 180)

def letter_q(t):
    line(t,100,90)
    line(t,50,0)
    line(t,100,270)
    line(t,50,180)
    back(t,50)
    line(t,25,135)
    back(t,50)

def letter_r(t):
    line(t,100, 90)
    line(t,50,0)
    line(t, 50, 270)
    line(t,50, 180)
    line(t, 85, 315)

def letter_s(t):
    line(t,50, 0)
    line(t,50, 90)
    line(t,50, 180)
    line(t,50, 90)
    line(t,50, 0)

def letter_t(t):
    line(t,100,90)
    line(t,50,180)
    back(t,100)

def letter_u(t):
    line(t,100,90)
    back(t,100)
    line(t,50,0)
    line(t,100,90)

def letter_v(t):
    line(t, 110,110)
    back(t, 110)
    line(t, 110, 70)

def letter_w(t):
    letter_v(t)
    line(t,110,290)
    line(t,110,70)
    
def letter_x(t):
    line(t,120,60)
    back(t,60)
    line(t,60,120)
    back(t,120)

def letter_y(t):
    line(t,120,60)
    back(t,60)
    line(t,60,120)

def letter_z(t):
    line(t,50,0)
    back(t,50)
    line(t,110,60)
    line(t,50,180)


# level 6 working on writing out a word 
def write(t):
    x = -300
    t.penup()
    t.setpos(x,0)
    word = str(input('Please give me a word'))
    for i in word:
        t.pendown()
        if i == 'a':
            letter_a(t)
        elif i == 'b':
            letter_b(t)
        elif i == 'c':
            letter_c(t)
        elif i == 'd':
            letter_d(t)   
        elif i == 'e':
            letter_e(t)
        elif i == 'f':
            letter_f(t)
        elif i == 'g':
            letter_g(t)
        elif i == 'h':
            letter_h(t)
        elif i == 'i':
            letter_i(t)
        elif i == 'j':
            letter_j(t)   
        elif i == 'k':
            letter_k(t)
        elif i == 'l':
            letter_l(t)
        elif i == 'm':
            letter_m(t)   
        elif i == 'n':
            letter_n(t)
        elif i == 'o':
            letter_o(t)
        elif i == 'p':
            letter_p(t)  
        elif i == 'q':
            letter_q(t)
        elif i == 'r':
            letter_r(t)
        elif i == 's':
            letter_s(t)   
        elif i == 't':
            letter_t(t)
        elif i == 'u':
            letter_u(t)
        elif i == 'v':
            letter_v(t)   
        elif i == 'w':
            letter_w(t)
        elif i == 'x':
            letter_x(t)
        elif i == 'y':
            letter_y(t)
        elif i == 'z':
            letter_z(t)  
        else:
            print('I can only do english alphabet characters!')
        t.penup()
        x = x + 70
        t.setpos(x, 0)



# a cheeky addition for level 7 is to do something like the line function above. 
# you need to import random to do this.

import random
def line(t,l,head):
    colours = ['black','green','red','blue']
    x = random.randint(0,3)
    t.pencolor(colours[x])
    t.setheading(head)
    t.fd(l)

