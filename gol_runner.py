import time
from gol import *

world = create_world(XSIZE, YSIZE)

def create_string(array):
    concat = ""
    #concat.join(str(x) for x in array)
    for x in array:
        concat += str(x)
    
world[10][10] = 1
print world[10][10]
print create_string(world[0])
#print 
