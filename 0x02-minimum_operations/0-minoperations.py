#!/usr/bin/python3
"""Python minimum operations"""


def minOperations(n: int) -> int:
    """
    Finds the minimum operations to reach `n#`

    Args:
    - n: an integer determning the number of occurences

    Returns:
    - the minimum  number of operations
    """
    if n <= 1:
        return 0
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return minOperations(i) + n // i
    return 0
