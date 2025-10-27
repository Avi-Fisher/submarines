

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
    count = 0

    for i in range(len(ships)):
        for j in range(len(ships)):
            if  ships and not shots:
                count += 1
    return count

def render_public(ships,shots):
    public_matrix = []

    for i in range(len(ships)):
        row = []

        for j in range(len(ships)):
            if ships[i][j] and shots[i][j]:
                row.append("V")
            elif shots[i][j]:
                row.append("X")
            else:
                row.append("O")

    return public_matrix

#  def renter_reveal(ships,shots):

























