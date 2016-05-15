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

def is_in_bounds(i, j, world):
    """Check if an index is out of bounds of the board."""
    if (i < 0 or j < 0 or i+1 > len(world) or j+1 > len(world[i])):
        return False
    else:
        return True

def num_neighbours(i, j, world):
    """Get number of neighbours of a cell."""
    neighbours = []

    for i1 in range(i-1, i+2):
        for j1 in range(j-1, j+2):
            if(is_in_bounds(i1, j1, world) and world[i1][j1] and not(i == i1 and j == j1)):
                neighbours.append(world[i1][j1])
    return len(neighbours)

#Runs a cell to its next iteration
def iterate_cell(i, j, world):
    """Run a game of life cell to its next iteration."""
    n = num_neighbours(i, j, world)
    cell = world[i][j]

    if(n < 2 and cell):
        return False
    elif(n < 4 and cell):
        return True
    elif(n > 4 and cell):
        return False
    elif(n == 3):
        return True
    else:
        return False

def next_iteration(world):
    """Run a game of life board to its next iteration."""
    #Build a new board.
    newWorld = []
    for i in range(0, len(world)):
        row = []
        for j in range(0, len(world[0])):
            row.append(iterate_cell(i, j, world))
        newWorld.append(row)
    return newWorld

def get_board_after(iterations, board):
    """Runs a board to a certain number of iterations."""
    for _ in range(0, iterations):
        board = next_iteration(board)

    return board
