#Conway's Game of Life Implementation
#Zachary Shannon - 05/2016

DEAD_CELL = '.'
ALIVE_CELL = '*'

#Checks for dead or alive.
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

#Test board.
conway=[['*','*','*','.','.'],
        ['*','.','.','*','.'],
        ['*','.','.','*','.'],
        ['.','.','*','*','.'],
        ['*','.','.','.','*']]

#Print it.
print2d(conway)

#Iterate on key press.
while True:
    input("Press any key")
    conway = nextIteration(conway)
    print2d(conway)
