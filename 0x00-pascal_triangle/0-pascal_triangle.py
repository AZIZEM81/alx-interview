#!/usr/bin/python3
"""
Implementation of the Pascal's triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]  # Start with the first row
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element of each row is always 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)  # Last element of each row is always 1
        triangle.append(new_row)
    return triangle
