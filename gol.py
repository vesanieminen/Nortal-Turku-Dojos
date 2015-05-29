from copy import deepcopy

XSIZE = 80
YSIZE = 25

def create_world(xsize, ysize):
    return [[0 for y in range(YSIZE)] for x in range(XSIZE)] 

def tick(world):
    original = deepcopy(world)
    for x in xrange(XSIZE):
        for y in xrange(YSIZE):
            count = neighbour_count(original, x, y)
            # rule 1: fewer than 2 neighbours => cell dies
            if count < 2:
                world[x][y] = 0
            # rule 2 & 4 combined
            if count == 3:
                world[x][y] = 1

def all_cells_are_dead(world):
    for x in xrange(XSIZE):
        for y in xrange(YSIZE):
            if world[x][y] != 0:
                return False
    return True
    
def neighbour_count(world, x, y):
    cells = []
    cells.append((x - 1, y - 1))
    cells.append((x, y - 1))
    cells.append((x + 1, y - 1))
    cells.append((x - 1, y))
    cells.append((x + 1, y))
    cells.append((x - 1, y + 1))
    cells.append((x, y + 1))
    cells.append((x + 1, y + 1))
    count = 0
    for cell in cells:
        if (cell[0] >= 0 and cell[0] < XSIZE) and (
           cell[1] >= 0 and cell[1] < YSIZE):
            if world[cell[0]][cell[1]] == 1:
                count += 1
    return count


