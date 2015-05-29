from copy import deepcopy

XSIZE = 80
YSIZE = 25

def create_world(xsize, ysize):
    return [[0 for x in range(XSIZE)] for x in range(YSIZE)] 

def tick(world):
    original = deepcopy(world)
    #for x in xrange(XSIZE):
    #    for y in xrange(YSIZE):
    world[10][10] = 0

def all_cells_are_dead(world):
    for x in xrange(XSIZE):
        for y in xrange(YSIZE):
            if world[y][x] != 0:
                return False
    return True
    
