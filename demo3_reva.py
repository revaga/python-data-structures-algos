import revaLab3

def run_test():
    with open("lists.html", "r") as file:
        parser = revaLab3.ListCollector()
        for line in file:
            parser.feed(line)
    print(parser.getLists())
    parser.close()


if __name__ == "__main__":
    run_test()

"""
[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 'Item three', 'Item four']]
"""
