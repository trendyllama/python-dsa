import pytest

from src.data_structures.linked_list import LinkedList, MissingNodeError


@pytest.fixture
def linked_list():
    return LinkedList()


def test_insert_empty_list(linked_list: LinkedList):
    linked_list.append(10)

    assert linked_list.head_node is not None
    assert linked_list.head_node.value == 10


def test_insert_non_empty_list(linked_list: LinkedList):
    linked_list.append(10)
    assert linked_list.head_node is not None
    assert linked_list.head_node.value == 10
    linked_list.append(20)

    assert linked_list.head_node is not None
    assert linked_list.head_node.value == 10
    assert linked_list.head_node.next_node is not None
    assert linked_list.head_node.next_node.value == 20


def test_insert_multiple_nodes(linked_list: LinkedList):
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    head = linked_list.head_node
    assert head is not None
    assert head.value == 10

    after_head = head.next_node
    assert after_head is not None
    assert after_head.value == 20

    after_after_head = after_head.next_node
    assert after_after_head is not None
    assert after_after_head.value == 30


@pytest.mark.parametrize("value", range(1, 100))
def test_larger_lists(linked_list: LinkedList, value: int) -> None:
    linked_list.append(value)
    assert linked_list.head_node is not None
    assert linked_list.head_node.value == value


def test_delete_empty_list(linked_list: LinkedList):
    linked_list.append(10)

    linked_list.append(30)

    with pytest.raises(MissingNodeError):
        linked_list.delete(10)

    linked_list.append(10)

    linked_list.delete(10)
    assert linked_list.head_node is not None
