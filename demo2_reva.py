import revaLab2


def run_test():
    for i in range (1,7):
        print("Row", i, end=": ")
        revaLab2.print_pascal(i)
        print()
    print("Reva's row: ", end="")
    revaLab2.print_pascal(11)


if __name__ == '__main__':
    run_test()

"""
Row 1: [1]
Row 2: [1, 1]
Row 3: [1, 2, 1]
Row 4: [1, 3, 3, 1]
Row 5: [1, 4, 6, 4, 1]
Row 6: [1, 5, 10, 10, 5, 1]
Reva's row: [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
"""