#!/usr/bin/python3
"""Pascal's Triangle"""

# cache to speed up factorial calculations
cache = {0: 1, 1: 1}

def factorial(n):
    """utility function to calculate factorial"""
    if n not in cache:
        cache[n] = n * factorial(n - 1)

    return cache[n]

def pascal_triangle(n):
    """Returns a matrix representing the pascal triangle"""
    # using the n choose k formula for finding a value
    # in any position in the pascal triangle
 
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            value = factorial(i) / (factorial(j) * factorial(i - j))
            row.append(value)
        triangle.append(row)

    return triangle
