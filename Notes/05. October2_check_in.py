""" We used if statements and or statements and elif and else
to create a FLOW OF EXECUTION """

def bot():
    x = str(input('How do you feel today? [G]ood/[B]ad'))
    if x == 'G' or x == 'g':
        print('Good to hear, I hope it continues!')
    elif x == 'B' or x == 'b':
        print('Aw no! That really sucks, I love you!')
    else:
        print('Sorry, I do not understand, try again?')
        bot()
