# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

def coin_reader(some_input):
    coins = 1
    some_input = some_input.lower()
    if some_input == 'y':
        return coins
    else:
        return None

 
def coin_lever(col, row):
    my_coins = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    if col == 1 and row == 2:
        counter1 += 1
        if counter1 <= 0:    
            coin_input = input("Pull a lever (y/n): ")
            my_coins = coin_reader(coin_input)

    elif col == 2 and row == 2:
        counter2 += 1
        if counter2 <= 0:    
            coin_input = input("Pull a lever (y/n): ")
            my_coins = coin_reader(coin_input)

    elif col == 2 and row == 3:
        counter3 += 1
        if counter3 <= 0:
            coin_input = input("Pull a lever (y/n): ")
            my_coins = coin_reader(coin_input)

    elif col == 3 and row == 2:
        counter4 += 1
        if counter4 <= 0:
            coin_input = input("Pull a lever (y/n): ")
            my_coins = coin_reader(coin_input)



# The main program starts here
victory = False
row = 1
col = 1

while not victory:
    valid_directions = find_directions(col, row)
    print_directions(valid_directions)
    victory, col, row = play_one_move(col, row, valid_directions)
print("Victory!")