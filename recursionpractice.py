def reverse(s=str):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def pascal_position(i, j):
    if i == 1 or j == 1 or i == j:
        return 1
    elif j == 0:
        return 0
    else:
        return pascal_position(i - 1, j - 1) + pascal_position(i - 1, j)


def printpascal(n):
    for i in range(1, n+1):
        print(pascal_position(n, i), end="")
    print()
printpascal(3)