from random import randint

def place_random_ships(ships,num):

    for n in range(num):
        num_ships1 = randint(0,len(ships))
        num_ships2 = randint(0,len(ships))

        ships[num_ships1][num_ships2] = 1





