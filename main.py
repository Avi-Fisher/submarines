from submarines.game import init_game
from submarines.io import print_status


def play():
    size = int(input("enter size number"))
    n_ships = int(input("enter ships number"))
    max_shots = int(input("enter how meny shots you have"))

    state = init_game(size,n_ships,max_shots)


    # while True:
    #     print_status(state)
    #     exit()



play()