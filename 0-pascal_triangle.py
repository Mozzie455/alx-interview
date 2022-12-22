#!/usr/bin/python3
"""
0x00-pascal_triangle
"""


def pascal_triangle(n):
    tr = []

    for i in range(n):
        tr.append([1]*(i+1))

    for i in range(2,n):
        for j in range(1, i):
            tr[i][j] = tr[i-1][j-1] + tr[i-1][j]

    return tr
