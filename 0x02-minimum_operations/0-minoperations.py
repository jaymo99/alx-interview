#!/usr/bin/python3
"""0-minioperations module"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in a file.
    """
    if n < 2:
        return 0

    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return sum(factors)
