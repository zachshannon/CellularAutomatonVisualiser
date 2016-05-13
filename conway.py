#Conway's Game of Life Implementation
#Zachary Shannon - 05/2016

import math

#TODO Needs a rewrite.
def open_board(file, aliveChar):
    """Reads in a board from a file. You MUST have a linebreak at the end of
    each line you want considered, so you must have a linebreak at the end of
    the last line too."""

    newBoard = []
    row = []

    f = open(file)

    while(True):
        c = f.read(1)
        if not c:
            #EOF
            break
        if(c == '\n'):
            #Add this row to the board, then clear.
            newBoard.append(row)
            row = []
        else:
            #Add this to the row.
            if(c == aliveChar):
                row.append(True)
            else:
                row.append(False)
    return newBoard

def build_board(rows, cols):
    """Constructs an empty board"""
    board = []

    for _ in range(rows):
        l = [False] * cols
        board.append(l)

    return board

def pad_board(rows, cols, board):
    """Takes the board board and puts it into the middle of an empty board of
    size rows * cols. You might get interesting results if the
    board is too big."""

    newBoard = build_board(rows, cols)

    startRow = math.ceil(rows/2) - math.ceil(len(board)/2)
    startCol = math.ceil(cols/2) - math.ceil(len(board[0])/2)

    for i, sublist in enumerate(board):
        for j, element in enumerate(sublist):
            newBoard[startRow + i][startCol + j] = board[i][j]

    return newBoard

def is_alive(cell):
    """Return true if cell is alive."""
    return(True if cell != False else False)
def is_dead(cell):
    """Return false if cell is dead."""
    return(not(is_alive(cell)))

def is_in_bounds(i, j, world):
    """Check if an index is out of bounds of the board."""
    if (i < 0 or j < 0 or i+1 > len(world) or j+1 > len(world[i])):
        return False
    else:
        return True

def get_neighbours(i, j, world):
    """Get a list of all neighbours of a cell."""
    neighbours = []

    #Look up
    if(is_in_bounds(i-1, j, world)):
        neighbours.append(world[i-1][j])
    #Look up left
    if(is_in_bounds(i-1, j-1, world)):
        neighbours.append(world[i-1][j-1])
    #Look up right
    if(is_in_bounds(i-1, j+1, world)):
        neighbours.append(world[i-1][j+1])
    #Look down
    if(is_in_bounds(i+1, j, world)):
        neighbours.append(world[i+1][j])
    #Look down left
    if(is_in_bounds(i+1, j-1, world)):
        neighbours.append(world[i+1][j-1])
    #Look down right
    if(is_in_bounds(i+1, j+1, world)):
        neighbours.append(world[i+1][j+1])
    #Look left
    if(is_in_bounds(i, j-1, world)):
        neighbours.append(world[i][j-1])
    #Look right
    if(is_in_bounds(i, j+1, world)):
        neighbours.append(world[i][j+1])

    return neighbours

#Find how many alive neighbours an element has.
def num_neighbours(i, j, world):
    """Count how many alive neighbours an element has."""
    n = 0
    for cell in get_neighbours(i, j, world):
        if is_alive(cell):
            n = n + 1
    return n

#Runs a cell to its next iteration
def iterate_cell(i, j, world):
    """Run a game of life cell to its next iteration."""
    n = num_neighbours(i, j, world)
    cell = world[i][j]

    if(n < 2 and is_alive(cell)):
        return False
    if(n < 4 and is_alive(cell)):
        return True
    if(n > 3 and is_alive(cell)):
        return False
    if(n == 3 and is_dead(cell)):
        return True

    return cell

def next_iteration(world):
    """Run a game of life board to its next iteration."""
    newWorld = world
    for i, sublist in enumerate(world):
        for j, element in enumerate(sublist):
            newWorld[i][j] = iterate_cell(i, j, world)
    return newWorld

def get_board_after(iterations, board):
    """Runs a board to a certain number of iterations."""
    for _ in range(0, iterations):
        board = next_iteration(board)

    return board
