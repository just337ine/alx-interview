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
    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
