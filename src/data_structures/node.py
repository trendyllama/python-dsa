"""
- only contains the Node class
"""

from typing import Any, Optional, Self


class Node:
    """
    - codecademy implementation of a node
    """

    def __init__(
        self,
        value: Any,
        next_node: Optional[Self] = None,
        prev_node: Optional[Self] = None,
    ) -> None:
        """
        - initialize the node with starting parameters
        - using the previous node property to support a
            linked list
        """

        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, link_node: Optional[Self]) -> Self:
        self.next_node = link_node

        return self

    def get_next_node(self) -> Optional[Self]:
        return self.next_node

    def get_value(self) -> Any:
        return self.value

    def set_prev_node(self, prev_node: Optional[Self]) -> Optional[Self]:
        """
        - this method supports a doubly linked list
        """

        match prev_node:
            case None:
                return None
            case Node():
                self.prev_node = prev_node
                return self

    def get_prev_node(self) -> Optional[Self]:
        match self.prev_node:
            case None:
                return None
            case Node():
                return self.prev_node
