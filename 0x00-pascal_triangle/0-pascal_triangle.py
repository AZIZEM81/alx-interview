#!/usr/bin/python3
"""
<<<<<<< HEAD
Module for generating Pascal's Triangle
=======
Module generating Pascal's Triangle
>>>>>>> 8c3b71e274935e08c46fed782fafe04956e8a5e0
"""

from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows to generate

    Returns:
        List[List[int]]: Pascal's Triangle as a list of lists of integers
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
