# This file contains the implementation of a queue data structure
# using the Node class from src/data_structures/node.py
from src.data_structures.node import Node

from .exceptions import EmptyQueueError


class Queue:
    """
    - codecademy implementation of a queue
    """

    def __init__(self) -> None:
        """
        - initializes a queue as empty by default

        Examples:
        >>> queue = Queue()
        >>> queue.head
        >>> queue.tail
        >>> queue.size
        0
        >>> queue.is_empty
        True
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.size
        3
        >>> queue.head.value
        1
        >>> queue.tail.value
        3

        """
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size: int = 0

    @property
    def head(self) -> Node | None:
        """
        - returns the head of the queue
        - the head is the first node in the queue

        Examples:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.head.value
        1
        """

        return self._head

    @head.setter
    def head(self, new_head: Node | None) -> None:
        self._head = new_head

    @property
    def tail(self) -> Node | None:
        """
        - returns the tail of the queue
        - the tail is the last node in the queue

        Examples:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.tail.value
        3
        """
        return self._tail

    @tail.setter
    def tail(self, new_tail: Node | None) -> None:
        self._tail = new_tail

    @property
    def size(self) -> int:
        """
        - returns the size of the queue

        Examples:
        >>> queue = Queue()
        >>> queue.size
        0
        >>> queue.enqueue(1)
        >>> queue.size
        1
        """
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size

    @property
    def is_empty(self) -> bool:
        """
        - returns True if the queue is empty, False otherwise

        Examples:
        >>> queue = Queue()
        >>> queue.is_empty
        True
        >>> queue.enqueue(1)
        >>> queue.is_empty
        False
        """
        return bool(self.head is None and self.tail is None)

    def _increase_size(self):
        """

        - increases the size of the queue by 1

        Examples:
        >>> queue = Queue()
        >>> queue.size
        0
        >>> queue.enqueue(1)
        >>> queue.size
        1
        """
        self.size += 1

    def _decrease_size(self):
        """
        - decreases the size of the queue by 1

        Examples:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.size
        1
        >>> queue.dequeue()
        >>> queue.size
        0
        """
        self.size -= 1

    def enqueue(self, value):
        """
        - adds a node to the end of the queue

        Examples:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.size
        3
        >>> queue.head.value
        1
        >>> queue.tail.value
        3
        """
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

            if self.head is None:
                raise RuntimeError

            self.head.next_node = self.tail

            self._increase_size()

            return None

        # this is the last node in the queue
        new_node = Node(value, self.tail, None)

        self.tail = new_node
        self._increase_size()
        assert self.size > 0

    def dequeue(self):
        """
        - removes the first node of the queue

        Examples:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.size
        3
        >>> queue.dequeue()
        >>> queue.size
        2
        >>> queue.head.value
        2
        >>> queue.tail.value
        3
        """
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

        if self.head is None or self.tail is None:
            raise RuntimeError

        self.head = self.head.next_node
        self._decrease_size()

    def peek(self):
        """

        - returns the value of the first node in the queue

        Examples:
        >>> queue = Queue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.size
        3
        >>> queue.peek()
        1
        """
        if self.is_empty:
            raise EmptyQueueError("Cannot peek from an empty queue")

        if self.head is None:
            raise RuntimeError

        return self.head.value

    def __len__(self):
        """
        - returns the size of the queue

        Examples:
        >>> queue = Queue()
        >>> len(queue)
        0
        >>> queue.enqueue(1)
        >>> len(queue)
        1
        """
        return self.size
