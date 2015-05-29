import pytest
from gol import XSIZE, YSIZE, tick, all_cells_are_dead, create_world

def test_world_can_be_created():
    world = create_world(XSIZE, YSIZE)

def test_cell_dies_with_fewer_than_two_live_neighbours():
    world = create_world(XSIZE, YSIZE)
    world[10][10] = 1
    tick(world)
    assert world[10][10] == 0, "A single cell in a world should die!"

def test_cell_with_two_or_three_neighbours_lives():
    world = create_world(XSIZE, YSIZE)
    x = 10
    y = 10
    world[x][y] = 1
    world[x + 1][y] = 1
    world[x + 2][y] = 1
    #  x
    # 111
    #  x
    tick(world)
    assert world[x + 1][y - 1] == 1
    assert world[x + 1][y + 1] == 1

def test_cell_with_more_than_three_neighbours_dies():
    world = create_world(XSIZE, YSIZE)
    x = 10
    y = 10
    world[x - 1][y] = 1
    world[x + 1][y] = 1
    world[x][y - 1] = 1
    world[x][y + 1] = 1
    #  1
    # 1x1
    #  1
    tick(world)
    assert world[x][y] == 0

def test_dead_cell_stay_dead():
    world = create_world(XSIZE, YSIZE)
    tick(world)
    assert all_cells_are_dead(world), "All the cells are not dead!"

    

