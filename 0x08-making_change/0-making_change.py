#!/usr/bin/python3
""" Making counts
"""


def makeChange(coins, total):
    """ find the number of coins needed
    Time: O(nlogn)
    """
    if total <= 0:
        return 0
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        increase = int(total / coin)
        total -= (increase * coin)
        count += increase
        if total == 0:
            return count

    return -1
