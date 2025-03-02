"""
- contains linked list class
"""

from src.data_structures.node import Node


class LinkedList:
    """
    - codecademy implementation of linked list
    """

    def __init__(self, head_node: Node | None = None) -> None:
        self._head_node = head_node

    @property
    def head_node(self) -> Node | None:
        return self._head_node

    @head_node.setter
    def head_node(self, new_head_node: Node | None) -> None:
        self._head_node = new_head_node

    @property
    def is_empty(self) -> bool:
        return self.head_node is None

    def append(self, new_node_value) -> None:
        if self.is_empty:
            self.head_node = Node(new_node_value, None)
            return

        current_node = self.head_node

        while current_node is not None:
            if current_node.next_node is None:
                current_node.next_node = Node(new_node_value, None)
                return
            current_node = current_node.next_node

    def delete(self, value_to_delete) -> None:
        if self.is_empty:
            return

        current_node = self.head_node

        while current_node is not None:
            if current_node.next_node is None:
                raise ValueError(f"Value {value_to_delete} not found in list")

            # want to look ahead by one node to see if the next node is the one to delete
            if current_node.next_node.value == value_to_delete:
                current_node.next_node = current_node.next_node.next_node
                return

            current_node = current_node.next_node
