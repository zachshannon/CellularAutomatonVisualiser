import draw
import conway
from PIL import Image

board = conway.open_board('golSeed.txt','O')

print("Run for a bit...")
board = conway.pad_board(50,50,board)
board = conway.get_board_after(150, board)

#Arbitrary colour scheme.
colours = [[174,141,204],[89,17,153],[201,202,255],[255,221,137],[204,179,141]]

img = draw.image_from_binary_random(board, 20, colours)
img.save('out.png', 'PNG')

cell = Image.open("cell.bmp")
img2 = draw.image_from_binary_cell(board, cell)
img2.save('out2.png', "PNG")

draw.print_2d(board, 'O', ' ')
