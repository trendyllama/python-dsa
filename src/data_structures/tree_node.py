"""
- module for treenode class
"""

from typing import Self


class TreeNode:
    """
    - codecademy implementation of treenode
    """

    def __init__(self, value) -> None:
        """
        - initializes a tree node with a value and an empty list of children

        Examples:
        >>> node = TreeNode(1)
        >>> node.value
        1
        >>> node.children
        []
        """
        self._value = value
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self) -> list[Self]:
        return self._children

    @children.setter
    def children(self, new_children: list[Self]) -> None:
        self._children = new_children

    def add_child(self, child_node: Self) -> None:
        """
        - adds a child node to the current node

        Examples:
        >>> parent_node = TreeNode(1)
        >>> child_node = TreeNode(2)
        >>> parent_node.add_child(child_node)
        """
        self.children.append(child_node)

    def remove_child(self, child_node: Self) -> None:
        """

        - removes a child node from the current node
        - if the child node is not in the list of children, it does nothing
        - if the child node is in the list of children, it removes it
        Examples:
        >>> parent_node = TreeNode(1)
        >>> child_node = TreeNode(2)
        >>> parent_node.add_child(child_node)
        >>> parent_node.remove_child(child_node)
        >>> parent_node.children
        []
        """
        self.children = list(filter(lambda x: x != child_node, self.children))

    def traverse(self, nodes_to_visit) -> None:
        print("Traversing...")
        nodes_to_visit = [self]

        if len(nodes_to_visit) < 0:
            return

        current_node = nodes_to_visit.pop()

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
