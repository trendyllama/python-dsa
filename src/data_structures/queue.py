from typing import Optional, Callable
from src.data_structures.node import Node


class EmptyQueueError(Exception):
    """
    Purpose:
        - exception to handle an empty queue
    """


class Queue:
    """
    - codecademy implementation of a queue
    """

    def __init__(self) -> None:

        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:

        return bool(self.head is None and self.tail is None)

    def enqueue(self, value) -> None:

        if self.is_empty():

            new_node = Node(value, None, None)
            self.size += 1
            self.head = new_node

            self.tail = new_node

            return

        new_node = Node(value, self.tail, None)

        self.size += 1
        self.tail = new_node

        return

    def dequeue(self) -> None:

        self.size -= 1

        if self.is_empty():

            raise EmptyQueueError("Cannot dequeue from an empty queue")

        self.head = self.head.get_prev_node()

    def peek(self) -> None:

        print(self.head.value)

    def print(self) -> Optional[Callable]:

        if self.is_empty():

            return

        self.peek()

        self.dequeue()

        return self.print()
