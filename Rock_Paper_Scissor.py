import random
import sys

def user_input():
    name = input('Enter your name player \t')
    inp = input('rock (r) , paper (p) , scissor (s) \t')
    if(inp not in ['r','p','s']):
        print ('Dude come on it\'s written what to enter')
        sys.exit()
    return name,inp

def pc_output():
    list = ['r','p','s']
    random.shuffle(list)
    return random.choice(list)

def winner(inp,pcinp,name):
    if(inp == 'r'):
        if (pcinp == 'p'):
            return 'PC is the winner'
    elif(inp == 'p'):
        if(pcinp == 's'):
            return 'PC is the winner'
    elif(inp == 's'):
        if(pcinp == 'r'):
            return 'PC is the winner'
    #print (pcinp)
    if (inp== pcinp):
        return 'Oh! Fax it\'s a draw'
    return name + ' is the winner'

user_name , user_inp = user_input()
pc_inp = pc_output()
print(winner(user_inp,pc_inp,user_name))

