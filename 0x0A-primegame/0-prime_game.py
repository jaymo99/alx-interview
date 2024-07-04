#!/usr/bin/python3
""" 0-prime_game module
"""


def memoize(f):
    """ Memoization decorator """
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper


@memoize
def sieve(n):
    """ Calculate all primes up to n using a simplified method """
    if n < 2:
        return []

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def isWinner(x, nums):
    """ Determine the winner of the game """
    if not nums or x <= 0:
        return None

    scores = {"Maria": 0, "Ben": 0}
    max_num = max(nums)
    all_primes = sieve(max_num)

    for n in nums:
        primes = [p for p in all_primes if p <= n]
        turn_count = len(primes)

        if turn_count % 2 == 0:
            scores["Ben"] += 1
        else:
            scores["Maria"] += 1

    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"
    else:
        return None
