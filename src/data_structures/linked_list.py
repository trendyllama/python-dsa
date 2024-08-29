"""
- contains linked list class
"""

from typing import Any, Optional
from src.data_structures.node import Node


class LinkedList:
    """
    - codecademy implementation of linked list
    """

    def __init__(self, head_node: Optional[Node] = None) -> None:
        """_summary_

        Args:
            head_node (Optional[Node], optional): _description_. Defaults to None.
        """
        self.head_node = head_node

    def insert(self, new_node) -> None:
        """_summary_

        Args:
            new_node (_type_): _description_
        """
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while current_node:
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self) -> Any:
        """_summary_

        Returns:
            Any: _description_

        Yields:
            Iterator[Any]: _description_
        """
        current_node = self.head_node

        while current_node:
            yield current_node.get_value()
            current_node = current_node.get_next_node()
