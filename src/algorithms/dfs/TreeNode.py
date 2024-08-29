from collections import deque
from typing import Any, Self


class TreeNode:
    """_summary_"""

    def __init__(self, value: Any):
        self.value: Any = value  # data
        self.children: list[Self] = []  # references to other nodes

    def __repr__(self):
        return self.value

    def add_child(self, child_node_value):
        """_summary_

        Args:
            child_node_value (_type_): _description_
        """
        # creates parent-child relationship
        print("Adding " + child_node_value)
        self.children.append(child_node_value)

    def remove_child(self, child_node_value):
        """_summary_

        Args:
            child_node_value (_type_): _description_
        """
        # removes parent-child relationship
        print("Removing " + child_node_value + " from " + self.value)
        self.children = list(filter(lambda x: x != child_node_value, self.children))

    def traverse(self):
        """_summary_"""
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

    def get_children(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.children

    def set_children(self, children):
        """_summary_

        Args:
            children (_type_): _description_
        """
        self.children = children


def print_tree(root: TreeNode):
    """_summary_

    Args:
        root (TreeNode): _description_
    """
    stack = deque()
    stack.append([root, 0])
    level_str = "\n"
    prev_level = 0
    level = 0
    while len(stack) > 0:
        prev_level = level
        node, level = stack.pop()

        if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
            level_str += "   " * (level - 1) + "├─"
        elif level > 0:
            level_str += "   " * (level - 1) + "└─"
        level_str += str(node.value)
        level_str += "\n"
        level += 1
        for child in node.children:
            stack.append([child, level])

    print(level_str)


def print_path(path):
    """_summary_

    Args:
        path (_type_): _description_
    """
    # If path is None, no path was found
    if path is None:
        print("No paths found!")

    # If a path was found, print path
    else:
        print("Path found:")
        for node in path:
            print(node.value)


sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]
