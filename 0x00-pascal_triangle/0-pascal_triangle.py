#!/usr/bin/python3
'''Mock interview question. Generating pascal triangle.
'''


def pascal_triangle(n):
    '''Creates a nested list of integers representing
    the Pascal's triangle.
    '''
    p_triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 0 and j > 0:
                row.append(p_triangle[i - 1][j - 1] + p_triangle[i - 1][j])
        p_triangle.append(row)
    return p_triangle
