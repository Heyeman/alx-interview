#!/usr/bin/python3
""" Making counts
"""


def makeChange(coins, total):
    """ find the number of coins needed
    Time: O(nlogn)
    """
    if total <= 0:
        return 0
    coins.sort()
    n = 0
    while coins:
        coin = coins.pop()
        if coin <= total:
            n += total//coin
            total %= coin
        if total == 0:
            return n
    return -1


print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
