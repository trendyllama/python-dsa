from typing import Optional, Self, Any

from src.data_structures.node import Node

from .exceptions import EmptyQueueError


class Queue:
    """
    - codecademy implementation of a queue
    """

    def __init__(self) -> None:
        """
        - initializes a queue as empty by default
        """
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    @property
    def head(self) -> Optional[Node]:
        return self._head

    @head.setter
    def head(self, new_head: Optional[Node]) -> None:
        self._head = new_head

    @property
    def tail(self) -> Optional[Node]:
        return self._tail

    @tail.setter
    def tail(self, new_tail: Optional[Node]) -> None:
        self._tail = new_tail

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size

    @property
    def is_empty(self) -> bool:
        return bool(self.head is None and self.tail is None)

    def _increase_size(self) -> Self:
        self.size += 1

        return self

    def _decrease_size(self) -> Self:
        self.size -= 1

        return self

    def enqueue(self, value):

        if self.is_empty:
            assert self.size == 0
            new_node = Node(value, None, None)

            self.head = new_node

            self.tail = new_node

            self._increase_size()

            return None

        if self.size == 1:
            new_node = Node(value, self.head, None)

            self.tail = new_node

            self.head.next_node = self.tail

            self._increase_size()

            return None

        # this is the last node in the queue
        new_node = Node(value, self.tail, None)

        self.tail = new_node
        self._increase_size()
        assert self.size > 0


    def dequeue(self):

        if self.is_empty:
            raise EmptyQueueError("Cannot dequeue from an empty queue")

        if self.size == 1:
            self.head = None
            self.tail = None
            self._decrease_size()

            return None

        if self.size == 2:
            self.head = self.tail
            self.tail = self.head
            self._decrease_size()

            return None

        self.head = self.head.next_node
        self.tail = self.tail.next_node
        self._decrease_size()


    def peek(self) -> Any:
        if self.is_empty:
            raise EmptyQueueError("Cannot peek from an empty queue")

        return self.head.value
