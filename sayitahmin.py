import random

number = random.randint(1,10)
chance = 5

def getdata():
    global user
    user = float(input('Guess a number:'))

while chance > 0:
    getdata()
    if user != number:
        chance = chance -1 
        print(f'That is wrong, you have {chance} more chances.')
        if user > number:
            print('lower')
        elif user < number:
            print('higher')
    else:
        print('Congratulations you win!')
        break
else:
    print(f'You chances are gone. Number was {number}')
