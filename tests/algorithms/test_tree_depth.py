import pytest

from src.algorithms.tree_depth import (
    breadth_first_search,
    build_bst,
    depth_first_search,
)
from src.data_structures.tree_node import TreeNode


def test_breadth_first_search_finds_root_and_children() -> None:
    root = TreeNode(4)
    left_child = TreeNode(2)
    right_child = TreeNode(6)
    root.add_child(left_child, "left")
    root.add_child(right_child, "right")

    assert breadth_first_search(root, root)
    assert breadth_first_search(root, left_child)
    assert breadth_first_search(root, right_child)


def test_breadth_first_search_returns_false_for_empty_or_missing_nodes() -> None:
    root = TreeNode(4)
    root.add_child(TreeNode(2), "left")

    assert breadth_first_search(None, root) is False
    assert breadth_first_search(root, TreeNode(8)) is False


def test_build_bst_returns_none_for_empty_list() -> None:
    assert build_bst([]) is None


def test_build_bst_builds_balanced_nested_dictionary() -> None:
    assert build_bst([1, 2, 3, 4, 5]) == {
        "data": 3,
        "left_child": {
            "data": 2,
            "left_child": {"data": 1, "left_child": None, "right_child": None},
            "right_child": None,
        },
        "right_child": {
            "data": 5,
            "left_child": {"data": 4, "left_child": None, "right_child": None},
            "right_child": None,
        },
    }


def test_depth_first_search_is_not_implemented() -> None:
    with pytest.raises(NotImplementedError, match="not implemented"):
        depth_first_search(TreeNode(1), 1)
