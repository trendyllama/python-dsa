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

    def __iter__(self) -> Iterator[Any]:
        current_node = self.head_node

        while current_node is not None:
            yield current_node.get_value()
            current_node = current_node.get_next_node()
