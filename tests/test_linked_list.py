from src.data_structures.linked_list import LinkedList
from src.data_structures.node import Node

def test_insert_empty_list():
    linked_list = LinkedList()
    linked_list.insert(10)

    assert linked_list.head_node is not None

    assert linked_list.head_node.get_value() == 10

def test_insert_non_empty_list():
    linked_list = LinkedList(Node(10))
    linked_list.insert(20)

    assert linked_list.head_node is not None
    assert linked_list.head_node.get_value() == 10
    assert linked_list.head_node.get_next_node() is not None
    assert linked_list.head_node.get_next_node().get_value() == 20

def test_iterate_list():
    linked_list = LinkedList(Node(10))
    linked_list.insert(20)
    linked_list.insert(30)
    values = [value for value in linked_list]
    assert values == [10, 20, 30]

def test_insert_multiple_nodes():
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    assert linked_list.head_node.get_value() == 10
    assert linked_list.head_node.get_next_node().get_value() == 20
    assert linked_list.head_node.get_next_node().get_next_node().get_value() == 30

def test_iterate_empty_list():
    linked_list = LinkedList()
    values = [value for value in linked_list]
    assert values == []