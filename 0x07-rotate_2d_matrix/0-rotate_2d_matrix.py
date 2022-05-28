#!/usr/bin/python3
""" Ritate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """ rotates a list 90 digree
    """
    # transpose the matrix
    # transposed = list(zip(*matrix))
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reversing the inner list
    for i in range(len(matrix)):
        low, high = 0, len(matrix[i]) - 1
        while (low < high):
            matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
            low += 1
            high -= 1


if __name__ == "__main__":
    mylist1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(mylist1)
    print(mylist1)
