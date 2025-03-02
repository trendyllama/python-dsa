"""
- contains stack class and exceptions related to the stack
"""

from typing import Any, Optional, Self

from .exceptions import EmptyStackError, StackOverflowError
from .node import Node


class Stack:
    """
    - codecademy implementation of a stack
    """

    def __init__(self) -> None:
        self._size: int = 0
        self._top_item: Optional[Node] = None
        self._limit: int = 1000

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size

    @property
    def top_item(self) -> Optional[Node]:
        return self._top_item

    @top_item.setter
    def top_item(self, new_top_item: Optional[Node]) -> None:
        self._top_item = new_top_item

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, new_limit: int) -> None:
        self._limit = new_limit

    def push(self, value: Any) -> Self:
        """
        - adds a node to the top of the stack
        """

        if self.has_space:
            item = Node(value)

            item.next_node = self.top_item
            self.top_item = item
            self.size += 1

            return self

        raise StackOverflowError

    def pop(self) -> None:
        """
        - removes the top node of the stack
        """

        if self.size > 0:
            item_to_remove = self.top_item

            if not isinstance(item_to_remove, Node):
                raise EmptyStackError

            self.top_item = item_to_remove.next_node
            self.size -= 1


        raise EmptyStackError

    def peek(self) -> Any:
        """
        - returns the value of the Node at the top of the stack
        """

        if self.size > 0 and isinstance(self.top_item, Node):
            return self.top_item.value

        raise EmptyStackError

    @property
    def has_space(self) -> bool:
        return self.limit > self.size

    @property
    def is_empty(self) -> bool:
        return self.size == 0


    def print(self) -> None:
        if not isinstance(self.top_item, Node):
            return None

        print(self.top_item.value)

        self.top_item = self.top_item.next_node

        return self.print()

    def __iter__(self) -> Self:
        self.current_node = self.top_item

        return self

    def __next__(self) -> Any:
        if not isinstance(self.current_node, Node):
            raise StopIteration

        value = self.current_node.value

        self.current_node = self.current_node.next_node

        return value

    def __len__(self) -> int:
        return self.size
