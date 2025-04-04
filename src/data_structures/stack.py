"""
- contains stack class and exceptions related to the stack
"""

from .exceptions import EmptyStackError, StackOverflowError
from .node import Node


class Stack:
    """
    - codecademy implementation of a stack
    """

    def __init__(self) -> None:
        self._size: int = 0
        self._head: Node | None = None
        self._limit: int = 1000

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size

    @property
    def head(self) -> Node | None:
        return self._head

    @head.setter
    def head(self, new_top_item: Node | None) -> None:
        self._head = new_top_item

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, new_limit: int) -> None:
        self._limit = new_limit

    def _increase_size(self) -> None:
        self.size += 1

    def _decrease_size(self) -> None:
        self.size -= 1

    def push(self, value) -> None:
        """
        - adds a node to the top of the stack
        """

        if self.is_empty:
            self.head = Node(value, None)
            self._increase_size()
            return

        if self.has_space:
            item = Node(value, self.head)

            self.head = item
            self._increase_size()
            return

        raise StackOverflowError

    def pop(self) -> None:
        """
        - removes the top node of the stack
        """

        if self.is_empty:
            raise EmptyStackError

        if self.size == 1:
            self.head = None
            self.size = 0
            return

        if self.head is None:
            raise RuntimeError

        self.head = self.head.next_node
        self._decrease_size()

    def peek(self):
        """
        - returns the value of the Node at the top of the stack
        """

        if self.head is None:
            raise RuntimeError

        if not self.is_empty:
            return self.head.value

        raise EmptyStackError

    @property
    def has_space(self) -> bool:
        return self.limit > self.size

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node.value
            current_node = current_node.next_node

    def __next__(self):
        return self.__iter__()

    def print(self) -> None:
        for node in self:
            print(node)
