import revaagarwalLab4


def run_test():
    tree = revaagarwalLab4.BinaryTree(3)
    tree.insert_right(7)
    tree.insert_right(6)
    tree.insert_right(5)
    tree.rightChild.leftChild = revaagarwalLab4.BinaryTree(4)

    tree.insert_left(1)
    tree.insert_left(2)

    print("Preorder Traversal:")
    tree.preorder()
    print()
    print("Inorder Traversal:")
    tree.inorder()
    print()
    print("Postorder Traversal:")
    tree.postorder()

    print()
    print("Max:", tree.find_max())
    print("Size:", tree.size())
    print("Height:", tree.height())


if __name__ == "__main__":
    run_test()

"""
Preorder Traversal:
3 2 1 5 4 6 7 
Inorder Traversal:
1 2 3 4 5 6 7 
Postorder Traversal:
1 2 4 7 6 5 3 
Max: 7
Size: 7
Height: 4
"""
