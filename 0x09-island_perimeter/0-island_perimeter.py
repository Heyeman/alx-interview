#!/usr/bin/python3
"""
Module find the perimeter of
and Island
"""


def island_perimeter(grid):
    """ return perimeter of island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if col - 1 == -1 or grid[row][col - 1] == 0:
                    perimeter += 1
                if len(grid[row]) == col + 1 or grid[row][col + 1] == 0:
                    perimeter += 1
                if row - 1 == -1 or grid[row - 1][col] == 0:
                    perimeter += 1
                if len(grid) == row+1 or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter
