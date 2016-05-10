#Conway's Game of Life Implementation
#Zachary Shannon - 05/2016

#Currently this will work with any 2D test board. Obviously a lot still needs to be done.

import math

from PIL import Image


DEAD_CELL = '.'
ALIVE_CELL = '*'

#Reads in a board. You MUST have a linebreak at the end of each line you
#want considered, so you must have a linebreak at the end of the last line too.
def openBoard(file):

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
            #Add this char to the row.
            row.append(c)
    return newBoard

#Constructs an empty board
def buildBoard(rows, cols):
    board = []

    for _ in range(rows):
        l = [DEAD_CELL] * cols
        board.append(l)

    return board

#Dunno how to explain what this does.
def padBoard(rows, cols, board):
    newBoard = buildBoard(rows, cols)

    startRow = math.ceil(rows/2) - math.ceil(len(board)/2)
    startCol = math.ceil(cols/2) - math.ceil(len(board[0])/2)

    for i, sublist in enumerate(board):
        for j, element in enumerate(sublist):
            newBoard[startRow + i][startCol + j] = board[i][j]

    return newBoard

#Checks for dead or alive - you spin me right round.
def isAlive(cell):
    return(True if cell != DEAD_CELL else False)
def isDead(cell):
    return(not(isAlive(cell)))

#Print out a 2d list.
def print2d(world):
    for sublist in world:
        for element in sublist:
            print(element, end='')
        print(""); #Newline

#Check if an element is out of bounds.
def isInBounds(i, j, world):
    if (i < 0 or j < 0 or i+1 > len(world) or j+1 > len(world[i])):
        return False
    else:
        return True

#Get the neighbours of a cell.
def getNeighbours(i, j, world):
    neighbours = []

    #Look up
    if(isInBounds(i-1, j, world)):
        neighbours.append(world[i-1][j])
    #Look up left
    if(isInBounds(i-1, j-1, world)):
        neighbours.append(world[i-1][j-1])
    #Look up right
    if(isInBounds(i-1, j+1, world)):
        neighbours.append(world[i-1][j+1])
    #Look down
    if(isInBounds(i+1, j, world)):
        neighbours.append(world[i+1][j])
    #Look down left
    if(isInBounds(i+1, j-1, world)):
        neighbours.append(world[i+1][j-1])
    #Look down right
    if(isInBounds(i+1, j+1, world)):
        neighbours.append(world[i+1][j+1])
    #Look left
    if(isInBounds(i, j-1, world)):
        neighbours.append(world[i][j-1])
    #Look right
    if(isInBounds(i, j+1, world)):
        neighbours.append(world[i][j+1])

    return neighbours

#Find how many alive neighbours an element has.
def numNeighbours(i, j, world):
    n = 0
    for cell in getNeighbours(i, j, world):
        if isAlive(cell):
            n = n + 1
    return n

#Runs a cell to its next iteration
def iterateCell(i, j, world):
    n = numNeighbours(i, j, world)
    cell = world[i][j]

    if(n < 2 and isAlive(cell)):
        return DEAD_CELL
    if(n < 4 and isAlive(cell)):
        return ALIVE_CELL
    if(n > 3 and isAlive(cell)):
        return DEAD_CELL
    if(n == 3 and isDead(cell)):
        return ALIVE_CELL

    return cell

#Take the world to its next iteration
def nextIteration(world):
    newWorld = world
    for i, sublist in enumerate(world):
        for j, element in enumerate(sublist):
            newWorld[i][j] = iterateCell(i, j, world)
    return newWorld


def getImage(world, cell):

    #There is a real potential for bugs here.

    #Load the cell.
    cellMap = cell.load()

    #Create a white image.
    img = Image.new('RGB', (len(world) * cell.size[0],
                                        len(world[0]) * cell.size[1]), "white")
    pixmap = img.load() #Create the pixel maps

    curRow = 0
    curCol = 0

    for i, sublist in enumerate(world):
        for j, element in enumerate(sublist):
            if (element == ALIVE_CELL):
                #Add to the map.
                for k in range (cell.size[0]):
                    for l in range (cell.size[1]):
                        pixmap[((j*cell.size[0])+l), ((i*cell.size[1])+k)] = cellMap[l, k]

    return img

#Test board.
iterations = 124
seed = openBoard('golSeed.txt')
conway = padBoard(50, 50, seed)

for _ in range(0, iterations):
    conway = nextIteration(conway)

# print2d(conway)
cell = Image.open('cell.bmp')
img = getImage(conway, cell)
img.save('out.png', "PNG")
