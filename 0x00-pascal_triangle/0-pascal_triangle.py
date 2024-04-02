#!/usr/bin/python3

'''
A function that that returns a list of
lists of integers representing the Pascal’s
triangle of n:
'''


def pascal_triangle(n):
    '''
    pascal triangle algorithm
    '''
    # Initialize an empty list
    triangle = []
    if n <= 0:
        # Return an empty list if n is non-positive val.
        return []

    for i in range(n):
        # First element of each row is always 1
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            # Calculate each element in the current row (except the first and last)
            # by summing the corresponding elements from the previous row.
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
                # Last element of each row is always 1
            row.append(1)
        triangle.append(row)

    return triangle
