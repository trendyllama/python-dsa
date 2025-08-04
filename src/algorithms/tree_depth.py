"""
- algos for trees
"""

from collections import deque

from src.data_structures.tree_node import TreeNode


def breadth_first_search(tree_node: TreeNode | None, value) -> bool:
    """
    - note: this function is recursive
    - returns a generator that yields the values of the tree in breadth-first order

    Examples:
    >>> root = TwoChildTreeNode(1).add_child(TwoChildTreeNode(2), "left").add_child(TwoChildTreeNode(3), "right")
    >>> breadth_first_search(root, 2)
    True
    >>> breadth_first_search(root, 4)
    False
    """

    if tree_node is None:
        return False

    queue = deque([tree_node])

    while queue:
        current_node = queue.popleft()

        if current_node == value:
            return True

        if current_node.left_child:
            queue.append(current_node.left_child)
        if current_node.right_child:
            queue.append(current_node.right_child)

    return False


def depth_first_search(tree_node: TreeNode, value) -> bool:
    """

    Examples:
    >>> root = TwoChildTreeNode(1).add_child(TwoChildTreeNode(2), "left").add_child(TwoChildTreeNode(3), "right")
    >>> depth_first_search(root, 2)
    True
    >>> depth_first_search(root, 4)
    False
    """

    raise NotImplementedError("This function is not implemented yet.")


def build_bst(my_list: list):
    """
    - note: this function is recursive
    - helper function to build trees


    Examples:
    >>> my_list = [1, 2, 3, 4, 5]
    >>> tree = build_bst(my_list)
    >>> tree['data']
    3
    >>> tree['left_child']['data']
    2
    >>> tree['right_child']['data']
    5
    """
    if len(my_list) == 0:
        return None

    mid_idx: int = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[:mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1 :])

    return tree_node
