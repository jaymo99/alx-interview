#!/usr/bin/python3
'''Mock interview question. Generating pascal triangle.
'''


def pascal_triangle(n):
    '''Creates a nested list of integers representing
    the Pascal's triangle.
    '''
    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        row = [1]
        if pascal_triangle:
            last_row = pascal_triangle[-1]
            row.extend([last_row[j] + last_row[j + 1]
                        for j in range(len(last_row) - 1)])
            row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
