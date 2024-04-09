#hf!usr/bin/python3
"""
Pascal Triangle
"""

def pascal_triangle(n):
    """ 
    Generate Pascal's Triangle up to the nth row

    Args:
    - n: an integer representing the number of rows in the triangle

    Returns:
    - a list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []
    #initialise triangle with the first one
    triangle = [[1]]

    for rows in range(1, n):
        row =  [1]
        for columns in range(1, rows):
            #calculates each value in the row based on the previous value
            row.append(triangle[rows-1][columns-1] + triangle[rows-1][columns])
        row.append(1)
        triangle.append(row)

    return triangle


    
