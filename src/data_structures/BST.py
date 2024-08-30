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
    """_summary_"""

    def __init__(self, value, depth=1):
        """_summary_

        Args:
            value (_type_): _description_
            depth (int, optional): _description_. Defaults to 1.
        """
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """

        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(
                    f"Tree node {value} added to the left of {self.value} at depth {self.depth + 1}"
                )
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(
                    f"Tree node {value} added to the right of {self.value} at depth {self.depth + 1}"
                )
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self.value == value:
            return self
        elif (self.left is not None) and (value < self.value):
            return self.left.get_node_by_value(value)
        elif (self.right is not None) and (value >= self.value):
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        """_summary_"""

        if self.left is not None:
            self.left.depth_first_traversal()

        print(f"Depth={self.depth}, Value={self.value}")

        if self.right is not None:
            self.right.depth_first_traversal()


print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
    tree.insert(random.randint(0, 100))

print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
