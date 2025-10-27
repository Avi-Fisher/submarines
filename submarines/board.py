from xmlrpc.client import Fault


def creat_matrix(num):
    matrix = []

    for i in range(num):
        row = []
        for j in range(num):
            row.append(0)

        matrix.append(row)
    return matrix

def creat_bool_matrix(num,bool=False):
    matrix = []

    for i in range(num):
        row = []

        for j in range(num):
            row.append(bool)

        matrix.append(row)
    return matrix

def in_bounds(size,x,y):
    if x > size or y > size or x < 0 or y < 0:
        return  False
    return True

def count_remaining_ships(ships,shots):
    count_ships = ships.count(1)
    count_bool = 0

    for i in range(len(ships)):
        for j in range(shots):
            if ships[i][j] and shots[i][j]:
                count_bool += 1

    return count_ships - count_bool

























