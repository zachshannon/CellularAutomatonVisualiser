#Tools for making pretty representations of grids of things.
#Zachary Shannon - 05/2016

#I'm running this on Ubuntu 14.04 Server.
#If this import doesn't work, well, good luck!
from PIL import Image
import random

def get_random_element(l):
    """Gets a random element from a list."""
    return l[random.randint(0, (len(l)-1))]

def image_from_binary_cell(world, cell):
    """Get image for a 2 dimensional binary array. Each 'True' element will
    be represented with the pixel map provided."""

    #Load the cell.
    cellMap = cell.load()

    #Create a white image.
    img = Image.new('RGB', (len(world[0]) * cell.size[0],
                                        len(world) * cell.size[1]), "white")
    pixmap = img.load() #Create the pixel maps

    curRow = 0
    curCol = 0

    for i, sublist in enumerate(world):
        for j, element in enumerate(sublist):
            if (element):
                #Add to the map.
                for k in range (cell.size[0]):
                    for l in range (cell.size[1]):
                        pixmap[((j*cell.size[0])+l), ((i*cell.size[1])+k)] = cellMap[l, k]

    return img

def image_from_binary_random(world, cellsize, colourScheme):
    """Get image for a 2 dimensional binary array. """

    #Create a white image.
    img = Image.new('RGB', (len(world[0]) * cellsize,
                                        len(world) * cellsize), "white")
    pixmap = img.load() #Create the pixel maps

    curRow = 0
    curCol = 0

    for i, sublist in enumerate(world):
        for j, element in enumerate(sublist):
            if (element):

                colour = get_random_element(colourScheme)

                #Add to the map.
                for k in range (cellsize):
                    for l in range (cellsize):
                        pixmap[((j*cellsize)+l), ((i*cellsize)+k)] = (colour[0], colour[1], colour[2])

    return img

def print_2d(world, alive, dead):
    """Print out a 2d list with the specified alive and dead characters."""
    for sublist in world:
        for element in sublist:
            if(element):
                print(alive, end='')
            else:
                print(dead, end='')
        print(""); #Newline
