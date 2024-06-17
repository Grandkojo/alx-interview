#!/usr/bin/python3
""" the island perimeter function """


def island_perimeter(grid):
    """ the island perimeter class
        grid: the grid to be used
        returns: the permeter of the island
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(0, rows-1):
        for col in range(0, cols-1):
            if grid[row][col] == 1
                # check top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # check botttom
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # check right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
