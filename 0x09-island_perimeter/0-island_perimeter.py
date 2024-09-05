#!/usr/bin/python3
"""
Island Perimeter:
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    perimeter = 0
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row] == 1:
                perimeter += 4
                if column > 0 and grid[column-1][row] == 1:
                    perimeter -= 2
                if row > 0 and grid[column][row-1] == 1:
                    perimeter -= 2
    return perimeter
