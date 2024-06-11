"""
Reva Agarwal
Sp24 Adv Data Struct/Algorithm Python
calculate pascal's triangle and print values based on position in triangle
"""


def print_pascal(n):
    """
    prints pascal's triangle by calculating values using pascal_position
    :param n: the row number of pascal's triangle starting from 1
    :return: doesn't return, but prints the values of the row of pascal's triangle
    """

    def pascal_position(i, j):
        """
        :param i: row value in pascal's triangle
        :param j: column value in pascal's triangle
        :return: value at a position in pascal's triangle
        """
        if i == 1 or j == 1 or i == j:
            return 1
        elif j == 0 or i == 0:
            return 0
        else:
            return pascal_position(i - 1, j - 1) + pascal_position(i - 1, j)

    print("[", end="")
    for l in range(1, n + 1):
        if l == n:
            print(pascal_position(n, l), end="]")
        else:
            print(pascal_position(n, l), end=", ")
