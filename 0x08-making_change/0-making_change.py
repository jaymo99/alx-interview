#!/usr/bin/python3
"""Coin Change Module
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to
    meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

                # Early exit if we have already reached the total
                if i == total and dp[i] != float('inf'):
                    return dp[i]

    return dp[total] if dp[total] != float('inf') else -1
