#!/usr/bin/python3
"""
a python module to sovle N-queens puzzle
"""
import sys


def display_queens(queens):
    """
    display_queens - function to display the solved queens
    Arguments:
        queens: the queens in row
    Return:
        nothing
    """
    for cord in queens:
        print(cord)


def checkSafety(x, y, safe_queens):
    """
    checkSafety - function to check the safety of the queens
                  it is safe when two queens are not in the same
                  row, column & diagonals
    Arguments:
        x: the x coordinate
        y: the y coordinate
        safe: the safe queens coordinate
    Returns:
        true if it is safe false otherwise
    """
    if safe_queens == []:
        return True
    rows = []
    cols = []
    for queen in safe_queens:
        rows.append(queen[0])
        cols.append(queen[1])
        denominator = x - queen[0]
        numerator = y - queen[1]
        m = 0
        if denominator != 0:
            m = abs(numerator / denominator)
        if m == 1:
            return False
    if x in rows or y in cols:
        return False
    return True


def place_queens(coor, y, n, safe_queens=[]):
    """
    place_queens - function to place a safety queens
    Arguments:
        coor: the given argument
        y: the y coordinate
        n: the number of queens
    Returns:
        list consists of safety queens
    """
    for x in range(n):
        if checkSafety(y, x, coor):
            coor.append([y, x])
            if y == n - 1:
                safe_queens.append(coor.copy())
                del coor[-1]
            else:
                place_queens(coor, y + 1, n)

    if len(coor):
        del coor[-1]
    return safe_queens


if __name__ == "__main__":
    """
    the main method to start execution
    """
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    """
    n = 6
    queens = []
    i = 0
    while i < n:
        j = 0
        coord = []
        while j < n:
            if j == 0:
                coord.append([j, i])
                j = j + 1
                continue
            k = 0
            while k < n:
                if checkSafety(j, k, coord):
                    coord.append([j, k])
                    break
                else:
                    k = k + 1
            j = j + 1
        if len(coord) == n:
            queens.append(coord)
        else:
            coord = []
        i = i + 1
    """
    coords = []
    queens = place_queens(coords, 0, n)
    display_queens(queens)