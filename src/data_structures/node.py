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
        """_summary_

        Args:
            value (Any): _description_
            next_node (Optional[Self], optional): _description_. Defaults to None.
            prev_node (Optional[Self], optional): _description_. Defaults to None.
        """

        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, link_node: Optional[Self]) -> None:
        """_summary_

        Args:
            link_node (Optional[Self]): _description_
        """
        self.next_node = link_node

    def get_next_node(self) -> Optional[Self]:
        """_summary_

        Returns:
            Optional[Self]: _description_
        """
        return self.next_node

    def get_value(self) -> Any:
        """_summary_

        Returns:
            Any: _description_
        """
        return self.value

    def set_prev_node(self, prev_node: Optional[Self]) -> None:
        """_summary_

        Args:
            prev_node (Optional[Self]): _description_

        Raises:
            TypeError: _description_
        """

        if prev_node is None:
            raise TypeError

        self.prev_node = prev_node

    def get_prev_node(self) -> Self:
        """_summary_

        Raises:
            TypeError: _description_

        Returns:
            Self: _description_
        """

        if not isinstance(self.prev_node, Node):
            raise TypeError

        return self.prev_node
