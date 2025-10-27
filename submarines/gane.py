def init_game(size,n_ships,max_shots,):

    state = {"size":size    ,
                 "ships":[],
                 "shots":[],
                 "n_ships":n_ships,
                 "max_shots":max_shots,
                 "shots_used":0}

    return state

def shoot(state,x,y):
    state["shots"][x][y] = True

    if state["ships"][x][y]:
        print("good shut")
    else:
        print("miss")

    state["shots_used"] += 1

    return state

def is_won(state):
    if state["n_ships"] == state["shots"].count(True):
        print("You win")

def is_lost(state):
    if state["max_shots"] == state["shots_used"]:
        print("You lose")



















