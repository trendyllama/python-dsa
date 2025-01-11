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
        self.size: int = 0
        self.top_item: Optional[Node] = None
        self.limit: int = 1000

    def push(self, value: Any) -> Self:
        """
        - adds a node to the top of the stack
        """

        match self.has_space():
            case True:
                item = Node(value)

                item.set_next_node(self.top_item)
                self.top_item = item
                self.size += 1

                return self

            case False:
                raise StackOverflowError

    def pop(self) -> None:
        """
        - removes the top node of the stack
        """

        match self.get_size() > 0:
            case True:
                item_to_remove = self.top_item

                if not isinstance(item_to_remove, Node):
                    raise EmptyStackError

                self.top_item = item_to_remove.get_next_node()
                self.size -= 1

            case False:
                raise EmptyStackError

    def peek(self) -> Any:
        """
        - returns the value of the Node at the top of the stack
        """

        if self.size > 0 and isinstance(self.top_item, Node):
            return self.top_item.get_value()

        raise EmptyStackError

    def has_space(self) -> bool:
        return self.limit > self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def print(self) -> None:
        if not isinstance(self.top_item, Node):
            return None

        print(self.top_item.get_value())

        self.top_item = self.top_item.get_next_node()

        return self.print()

    def __iter__(self) -> Self:
        self.current_node = self.top_item

        return self

    def __next__(self) -> Any:
        if not isinstance(self.current_node, Node):
            raise StopIteration

        value = self.current_node.get_value()

        self.current_node = self.current_node.get_next_node()

        return value

    def __len__(self) -> int:
        return self.get_size()
