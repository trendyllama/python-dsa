"""
- module for treenode class
"""

from typing import Any, Self


class EmptyTreeError(Exception):
    """
    - exception for handling an empty tree
    """


class TreeNode:
    """
    - codecademy implementation of treenode
    """

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []

    def add_child(self, child_node: Self) -> None:

        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node: Self) -> None:

        print(f"Removing {child_node.value} from {self.value}")
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self) -> None:
        print("Traversing...")
        nodes_to_visit = [self]

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


class StoryTreeNode:
    """
    - treenode class for sorted tale
    """

    def __init__(self, story_piece) -> None:
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node: Self) -> None:
        self.choices.append(node)

    def traverse(self) -> None:
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
