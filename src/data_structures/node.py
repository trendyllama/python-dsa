"""
- only contains the Node class
"""

from typing import Optional, Any, Self


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
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, link_node: Self) -> None:
        self.next_node = link_node

    def get_next_node(self) -> Optional[Self]:
        return self.next_node

    def get_value(self) -> Any:
        return self.value

    def set_prev_node(self, prev_node: Self) -> None:
        self.prev_node = prev_node

    def get_prev_node(self) -> Self:

        if not isinstance(self.prev_node, Node):
            raise TypeError

        return self.prev_node
