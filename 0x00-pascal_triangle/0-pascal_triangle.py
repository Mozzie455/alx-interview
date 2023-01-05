#!/usr/bin/python3
"""
    Returns a list of lists of integers representing the Pascal's triangle of n.

    If n is less than or equal to 0, returns an empty list.

    Args:
    - n: an integer

    Returns:
    - a list of lists of integers
    """

def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle

    triangle.append([1])
    for i in range(1, n):
        prev_row = triangle[i-1]
        curr_row = []
        curr_row.append(1)
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)
    return triangle