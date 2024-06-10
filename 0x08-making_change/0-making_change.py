#!/usr/bin/python3
"""This is making change problem solution"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given
    amount `total`

    Args:
        coins (_type_): _description_
        total (_type_): _description_
    """
    if total <= 0:
        return 0

    value = total
    coins.sort()
    index = len(coins) - 1
    ans = []

    while index >= 0:
        while value >= coins[index]:
            value -= coins[index]
            ans.append(coins[index])
        index -= 1

    if total != sum(ans):
        return -1

    return len(ans)
