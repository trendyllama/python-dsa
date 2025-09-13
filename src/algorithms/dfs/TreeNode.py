
import logging
from collections import deque
from typing import Self

logger = logging.getLogger(__name__)


class TreeNode:
    """

    Example:
    >>> root = TreeNode(1)
    >>> child1 = TreeNode(2)
    >>> child2 = TreeNode(3)
    >>> root.children = [child1, child2]
    >>> child1.children = [TreeNode(4), TreeNode(5)]
    >>> child2.children = [TreeNode(6)]
    >>> root.value
    1
    >>> child1.value
    2
    >>> child2.value
    3
    >>> root.children[0].value
    2
    """

    def __init__(self, value):
        self.value = value  # data
        self.children: list[Self] = []  # references to other nodes

    def __repr__(self):
        return self.value

    def add_child(self, child_node_value):
        """
        Example:
        >>> root = TreeNode("A")
        >>> child = TreeNode("B")
        >>> root.add_child(child)
        >>> root.children[0].value
        'B'
        """
        # creates parent-child relationship
        self.children.append(child_node_value)

    def remove_child(self, child_node_value):
        # removes parent-child relationship
        logger.info("Removing %s from %s", child_node_value, self.value)
        self.children = list(filter(lambda x: x != child_node_value, self.children))

    def traverse(self):
        """
        Example:

        """
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            logger.info(current_node.value)
            nodes_to_visit += current_node.children

    def get_children(self):
        return self.children

    def set_children(self, children):
        self.children = children


def print_tree(root: TreeNode):
    stack = deque()
    stack.append([root, 0])
    level_str = "\n"
    level = 0
    while len(stack) > 0:
        node, level = stack.pop()

        if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
            level_str += f"{'   ' * (level - 1)}├─"
        elif level > 0:
            level_str += f"{'   ' * (level - 1)}└─"
        level_str += str(node.value)
        level_str += "\n"
        level += 1
        for child in node.children:
            stack.append([child, level])

    logger.info(level_str)


def print_path(path):
    # If path is None, no path was found
    if path is None:
        logger.info("No paths found!")

    # If a path was found, print path
    else:
        logger.info("Path found:")
        for node in path:
            logger.info(node.value)
