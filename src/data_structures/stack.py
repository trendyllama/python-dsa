"""
- contains stack class and exceptions related to the stack
"""

from src.data_structures.exceptions import EmptyStackError, StackOverflowError
from src.data_structures.node import Node


class Stack:
    """
    - codecademy implementation of a stack
    """

    def __init__(self) -> None:
        """
        - initializes a stack as empty by default

        Examples:
        >>> stack = Stack()
        >>> stack.head
        >>> stack.size
        0
        >>> stack.is_empty
        True
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.size
        3
        >>> stack.head.value
        3
        >>> stack.head.next_node.value
        2
        >>> stack.head.next_node.next_node.value
        1
        """
        self._size: int = 0
        self._head: Node | None = None
        self._limit: int = 1000

    @property
    def size(self) -> int:
        """
        - returns the size of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.size
        0
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.size
        3
        >>> stack.pop()
        >>> stack.size
        2
        """
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        if not isinstance(new_size, int):
            msg = "Size must be an integer"
            raise TypeError(msg)

        if new_size < 0:
            msg = "Size cannot be negative"
            raise ValueError(msg)

        self._size = new_size

    @property
    def head(self) -> Node | None:
        """
        - returns the head node of the stack
        - the head node is the top of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.head
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.head.value
        3
        """
        return self._head

    @head.setter
    def head(self, new_top_item: Node | None) -> None:
        self._head = new_top_item

        return None

    @property
    def limit(self) -> int:
        """
        - returns the limit of the stack
        - the limit is the maximum size of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.limit
        1000
        >>> for i in range(1000):
        ...     stack.push(i)
        >>> stack.limit
        1000
        >>> stack.push(1001)
        Traceback (most recent call last):
        src.data_structures.exceptions.StackOverflowError
        """
        return self._limit

    @limit.setter
    def limit(self, new_limit: int) -> None:
        self._limit = new_limit

        return None

    def _increase_size(self) -> None:
        self.size += 1

        return None

    def _decrease_size(self) -> None:
        self.size -= 1
        return None

    def push(self, value) -> None:
        """
        - adds a node to the top of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.size
        3
        >>> stack.head.value
        3
        """

        if self.is_empty:
            self.head = Node(value, None)
            self._increase_size()
            return None

        if self.has_space:
            item = Node(value, self.head)

            self.head = item
            self._increase_size()
            return None

        raise StackOverflowError

    def pop(self) -> None:
        """
        - removes the top node of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.size
        3
        >>> stack.pop()
        >>> stack.size
        2
        >>> stack.head.value
        2
        """

        if self.is_empty:
            raise EmptyStackError

        if self.size == 1:
            self.head = None
            self.size = 0
            return None

        if self.head is None:
            raise RuntimeError

        self.head = self.head.next_node
        self._decrease_size()

        return None

    def peek(self):
        """
        - returns the value of the Node at the top of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> stack.size
        3
        >>> stack.peek()
        3
        """

        if self.head is None:
            raise RuntimeError

        if not self.is_empty:
            return self.head.value

        raise EmptyStackError

    @property
    def has_space(self) -> bool:
        """
        - returns True if the stack has space to add a new node

        Examples:
        >>> stack = Stack()
        >>> stack.has_space
        True
        >>> for i in range(1000):
        ...     stack.push(i)
        >>> stack.size
        1000
        >>> stack.has_space
        False
        """
        return self.limit > self.size

    @property
    def is_empty(self) -> bool:
        """
        - returns True if the stack is empty

        Examples:
        >>> stack = Stack()
        >>> stack.is_empty
        True
        >>> stack.push(1)
        >>> stack.is_empty
        False
        """
        return self.size == 0

    def __iter__(self):
        """
        - returns an iterator for the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> for value in stack:
        ...     print(value)
        3
        2
        1
        """
        current_node = self.head

        while current_node:
            yield current_node.value
            current_node = current_node.next_node

    def __next__(self):
        """

        - returns the next value in the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> next(stack)
        3
        >>> next(stack)
        2
        >>> next(stack)
        1
        """

        if self.head is None:
            raise StopIteration
        value = self.head.value
        self.head = self.head.next_node
        self._decrease_size()
        return value

    def __str__(self) -> str:
        """
        - returns the string representation of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> print(stack)
        3 -> 2 -> 1
        """
        return " -> ".join(map(str, self))

    def __len__(self) -> int:
        """
        - returns the length of the stack

        Examples:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> len(stack)
        3
        """
        return self.size
