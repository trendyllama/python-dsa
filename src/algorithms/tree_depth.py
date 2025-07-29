"""
- algos for trees
"""

from collections.abc import Callable

from src.data_structures.tree_node import TreeNode


def depth(tree_node: TreeNode | None) -> Callable | None:
    """
    - note: this function is recursive
    - returns the depth of the tree as an integer


    """

    if tree_node is None:
        return

    left_depth = depth(tree_node["left_child"])
    right_depth = depth(tree_node["right_child"])

    if left_depth > right_depth:
        return left_depth + 1

    return right_depth + 1


def build_bst(my_list: list):
    """
    - note: this function is recursive
    - helper function to build trees
    """
    if len(my_list) == 0:
        return None

    mid_idx: int = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[:mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1 :])

    return tree_node


def test_cases_tree() -> None:
    """
    - test cases
    - helper variables
    """

    tree_level_1 = build_bst([1])
    tree_level_2 = build_bst([1, 2, 3])
    tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    assert depth(tree_level_1) == 1
    assert depth(tree_level_2) == 2
    assert depth(tree_level_4) == 4


if __name__ == "__main__":
    """
    - run test cases
    """
    test_cases_tree()
