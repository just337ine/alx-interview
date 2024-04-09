#!/usr/bin/python3
"""
    A method that calculates the fewest
    number of operations needed to result in
    exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
        prototype: def minOperations(n)
        Return an integer
        if n is impossible to achieve, return 0
    """
    if n < 2:
        return 0

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n]
