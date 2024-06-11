"""
Reva Agarwal
Sp24 Adv Data Struct/Algorithm Python
Binary trees and algorithm to recursively find maximum element in them
"""


class BinaryTree:
    """
    class to create binary trees
    """

    def __init__(self, root):
        """
        initialize the tree
        :param root: the root element in a binary tree
        """
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, node):
        """
        inserting a node to the left side of a tree
        :param node: node to be added
        :return: nothing
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, node):
        """
        inserting a node to the right side of the tree
        :param node: node to be added
        :return: nothing
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_val(self, root):
        self.root = root

    def get_root_val(self):
        return self.root

    def search(self, data):
        """
        recursively search whether an element is in the tree
        :param data: data to search for
        :return: T/F if element was found
        """
        if self.root == data:
            return True
        if self.leftChild:
            if self.leftChild.search(data):
                return True
        if self.rightChild:
            if self.rightChild.search(data):
                return True
        return False

    def preorder(self):
        """
        traverses tree in preorder
        :return: prints preorder
        """
        print(self.root, end=" ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        """
        traverses tree in inorder
        :return: prints inorder
        """
        if self.leftChild:
            self.leftChild.inorder()
        print(self.root, end=" ")
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        """
        traverses tree in postorder
        :return: prints postorder traversal
        """
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.root, end=" ")

    def size(self):
        """
        recursively calls and adds 1 for each element
        :return: size of tree
        """
        size = 1
        if self.leftChild:
            size += self.leftChild.size()
        if self.rightChild:
            size += self.rightChild.size()
        return size

    def height(self):
        """
        recursively calls and calculates height
        :return: height of tree
        """
        if self.leftChild:
            left_height = self.leftChild.height()
        else:
            left_height = 0
        if self.rightChild:
            right_height = self.rightChild.height()
        else:
            right_height = 0
        return max(left_height, right_height) + 1

    def find_max(self):
        """
        traverses through tree and compares to find max
        time complexity: O(number of nodes)
        space complexity: O(height of tree)
        :return: max data from tree
        """
        if self.root is None:
            return 0
        max_val = self.root
        if self.leftChild:
            max_val = max(max_val, self.leftChild.find_max())
        if self.rightChild:
            max_val = max(max_val, self.rightChild.find_max())
        return max_val

    def delete(self, node, data):
        """
        deletes node from tree by replacing the node and
        moving its child nodes around
        :param node: current node
        :param data: data to be deleted
        :return:
        """
        if not node:
            return None

        if data < node.root:
            node.leftChild = self.delete(node.leftChild, data)
        elif data > node.root:
            node.rightChild = self.delete(node.rightChild, data)
        else:
            # Node to be deleted found
            if not node.leftChild:
                return node.rightChild
            elif not node.rightChild:
                return node.leftChild
            else:
                # Node has both children
                small = self.find_min(node.rightChild)
                node.root = small.key
                node.rightChild = self.delete(node.rightChild, small.key)
        return node

    def find_min(self, node):
        """
        starting from a node, find_min returns the
        minimum element in the tree (if the tree is set up well)
        :param node: initial node
        :return: minimum element from a starting node
        """
        while node.leftChild:
            node = node.leftChild
        return node
