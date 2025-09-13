"""
- module for treenode class
"""

from typing import Literal, Self


class TreeNode:
    """
    - treenode class for two value tree
    """

    def __init__(self, value) -> None:
        self.value = value
        self.left_child: Self | None = None
        self.right_child: Self | None = None

    def add_child(self, child: Self, left_or_right: Literal["left", "right"]) -> Self:
        """
        - adds a child to the left or right child of the current node
        - if the left or right child is already set, it raises an error

        Examples:
        >>> node = TreeNode(1).add_child(TreeNode(2), "left")
        """
        if left_or_right == "left":
            if self.left_child is not None:
                raise ValueError("Left child already exists.")
            self.left_child = child
        elif left_or_right == "right":
            if self.right_child is not None:
                raise ValueError("Right child already exists.")
            self.right_child = child
        else:
            raise ValueError("left_or_right must be 'left' or 'right'.")

        return self


class StoryTreeNode:
    """
    - treenode class for sorted tale
    """

    def __init__(self, story_piece) -> None:
        self.story_piece = story_piece
        self.choices: list[Self] = []

    def add_child(self, node: Self) -> None:
        self.choices.append(node)

    def traverse(self) -> None:
        """
        - traverses the story tree and prints the story piece
        - prints the story piece and the choices
        """
        story_node = self
        print(story_node.story_piece)

        while story_node.choices:
            choice = input("Enter 1 or 2 to continue the story: ")

            if choice not in ["1", "2"]:
                print("Please choice 1 or 2!")
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child: Self = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child
