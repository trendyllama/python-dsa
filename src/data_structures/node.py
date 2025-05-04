"""
- only contains the Node class
"""

from typing import Self


class Node:
    """
    - codecademy implementation of a node
    """

    def __init__(
        self,
        value,
        next_node: Self | None = None,
        prev_node: Self | None = None,
    ) -> None:
        """
        - initialize the node with starting parameters
        - using the previous node property to support a
            linked list

        Examples:
        >>> node = Node(1)
        >>> node.value
        1
        >>> node.next_node
        >>> node.next_node = Node(2)
        >>> node.next_node.value
        2
        >>> node.previous_node
        >>> node.previous_node = Node(0)
        >>> node.previous_node.value
        0
        """

        self._value = value
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def next_node(self) -> Self | None:
        if self._next_node is None:
            return None

        return self._next_node

    @next_node.setter
    def next_node(self, link_node: Self | None) -> None:
        self._next_node = link_node

    @property
    def previous_node(self) -> Self | None:
        if self._prev_node is None:
            return None

        return self._prev_node

    @previous_node.setter
    def previous_node(self, link_node: Self | None) -> None:
        self._prev_node = link_node

    @property
    def value(self):
        '''
        - returns the value of the node

        Examples:
        >>> node = Node(1)
        >>> node.value
        1
        >>> node.value = 2
        >>> node.value
        2
        '''
        if self._value is None:
            return None

        return self._value

    @value.setter
    def value(self, new_value) -> None:
        self._value = new_value
