import random

def list_of_people():
    n = int(input('How many players wanna slog their arses '))
    players_list = []
    print ('Can I get all the players ')
    for i in range(n):
        players_list.append(input('Player '+str(i+1)+' - '))
    print ('Cool')
    return players_list,n

def random_team(list,n):
    random.shuffle(list)
    team1 = []
    team2 = []
    chance = 1

    for x in list:
        if chance==1:
            team1.append(x)
            chance = 0
        else:
            team2.append(x)
            chance = 1
    list.remove(x)
    return team1,team2

players,len = list_of_people()
a,b = random_team(players,len)
print('Team 1st is '+str(a))
print('Team 2nd is '+str(b))




