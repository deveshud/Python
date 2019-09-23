# 1st Python Project
import random

# Taking user input
def user_input():
    x = raw_input('Please enter \'Y\' to roll the dice otherwise any keyword to exit\n')
    return x

# Generating random  number
def generate_randomnumber():
    #dice_numbers = [1,2,3,4,5,6]
    #random.shuffle(dice_numbers)
    #print (random.choice(dice_numbers))
    #return random.choice(dice_numbers)
    return random.randrange(1,7,1)

a = user_input()
while a.upper() == 'Y' :
    print('Random number generated is '+str(generate_randomnumber()))
    a = user_input()
    
    
print ('Thank you')

