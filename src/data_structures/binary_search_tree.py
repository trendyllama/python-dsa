"""

If the new value is less than the root node's value
  If a left child node does not exist
    Create a new BinarySearchTree with the new value and updated depth and assign it to the left pointer
  Else
    Recursively call .insert() on the left child node
Else
  If a right child node does not exist
    Create a new BinarySearchTree with the new value and updated depth and assign it to the right pointer
  Else
    Recursively call .insert() on the right child node

Insert 50
50 < 100, left child node doesn't exist, create a left child node with value 50 and depth 2

    ==> 100
       /
      50

Insert 125
125 > 100, right child node doesn't exist, create a right child node with value 125 and depth 2

    ==> 100
       /   \
      50    125

Insert 75
75 < 100, left child node with value 50 exists, recursively insert at left child

    ==> 100
       /   \
      50    125

75 > 50, right child node doesn't exist, create a right child node with value 75 and depth 3

        100
       /   \
  ==> 50    125
       \
       75

Insert 25
25 < 100, left child node with value 50 exists, recursively insert at left child

    ==> 100
       /   \
      50    125
        \
        75

25 < 50, left child node doesn't exist, create a left child node with value 25 and depth 3

        100
       /   \
  ==> 50    125
     /  \
    25  75


"""

import random


class BinarySearchTree:
    def __init__(self, value, depth=1):
        '''
        - initializes a binary search tree with a value and depth
        - the depth is 1 for the root node
        - the depth is incremented by 1 for each child node
        - the left child node is less than the parent node
        - the right child node is greater than or equal to the parent node
        - the left and right child nodes are initialized to None

        Examples:
        >>> tree = BinarySearchTree(100)
        >>> tree.value
        100
        >>> tree.depth
        1
        >>> tree.left
        >>> tree.right
        >>> tree.insert(50)
        >>> tree.left.value
        50
        >>> tree.left.depth
        2
        >>> tree.insert(125)
        >>> tree.right.value
        125
        >>> tree.right.depth
        2
        '''
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(
                    f"Tree node {value} added to the left of {self.value} at depth {self.depth + 1}"
                )
            else:
                self.left.insert(value)
        else:
            match self.right:
                case None:
                    self.right = BinarySearchTree(value, self.depth + 1)
                    print(
                        f"Tree node {value} added to the right of {self.value} at depth {self.depth + 1}"
                    )
                case _:
                    self.right.insert(value)

    def get_node_by_value(self, value):
        if self.value == value:
            return self
        elif (self.left is not None) and (value < self.value):
            return self.left.get_node_by_value(value)
        elif (self.right is not None) and (value >= self.value):
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if self.left is not None:
            self.left.depth_first_traversal()

        print(f"Depth={self.depth}, Value={self.value}")

        if self.right is not None:
            self.right.depth_first_traversal()


if __name__ == "__main__":
    # Example usage
    print("Creating Binary Search Tree rooted at value 100:")
    tree = BinarySearchTree(100)

    for x in range(10):
        tree.insert(random.randint(0, 100))

    print("Printing the inorder depth-first traversal:")
    tree.depth_first_traversal()
