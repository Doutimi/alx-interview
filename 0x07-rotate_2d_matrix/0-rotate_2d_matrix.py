#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(m):
    """Rotates 90 degrees clockwise a matrix in place.
    Args:
        m: n x n matrix.
    """

    n = len(m[0])

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = m[i][j]
            # Moves the element from the left column to the top row
            m[i][j] = m[n - 1 - j][i]
            # Moves the element from the bottom row to the left column
            m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j]
            # Moves the element from the right column to the bottom row
            m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i]
            m[j][n - 1 - i] = temp
