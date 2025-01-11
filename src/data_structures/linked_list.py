"""
- contains linked list class
"""

from typing import Any, Iterator, Optional

from src.data_structures.node import Node


class LinkedList:
    """
    - codecademy implementation of linked list
    """

    def __init__(self, head_node: Optional[Node] = None) -> None:
        self.head_node = head_node

    def insert(self, new_node_value: Any) -> None:
        current_node = self.head_node

        if current_node is None:
            self.head_node = Node(new_node_value)

        while current_node is not None:
            next_node = current_node.get_next_node()

            if not next_node:
                current_node.set_next_node(new_node_value)
            current_node = next_node

    def delete(self, value_to_delete: Any) -> None:
        if self.head_node is None:
            raise ValueError("List is empty")

        current_node = self.head_node

        if current_node.get_value() == value_to_delete:
            self.head_node = current_node.get_next_node()

        while current_node:
            next_node = current_node.get_next_node()

            if next_node is None:
                break

            if next_node.get_value() == value_to_delete:
                current_node.set_next_node(next_node.get_next_node())
                current_node = None
            else:
                current_node = next_node

    def stringify_list(self) -> str:
        current_node = self.head_node
        result = []

        while current_node:
            result.append(current_node.get_value())
            current_node = current_node.get_next_node()

        return " -> ".join(result)

    def __str__(self) -> str:

        return self.stringify_list()

    def __iter__(self) -> Iterator[Any]:
        self.current_node = self.head_node

        return self

    def __next__(self) -> Any:

        if self.current_node is None:
            raise StopIteration

        value = self.current_node.get_value()
        self.current_node.get_next_node()

        return value
