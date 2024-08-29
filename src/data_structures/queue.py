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
        """_summary_"""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """

        return bool(self.head is None and self.tail is None)

    def enqueue(self, value) -> None:
        """_summary_

        Args:
            value (_type_): _description_
        """

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
        """_summary_

        Raises:
            EmptyQueueError: _description_
            TypeError: _description_
        """

        self.size -= 1

        if self.is_empty():

            raise EmptyQueueError("Cannot dequeue from an empty queue")

        if self.head is None:
            raise TypeError

        self.head = self.head.get_prev_node()

    def peek(self) -> None:
        """_summary_

        Raises:
            TypeError: _description_
        """

        if self.head is None:
            raise TypeError

        print(self.head.value)

    def print(self) -> Optional[Callable]:
        """_summary_

        Returns:
            Optional[Callable]: _description_
        """

        if self.is_empty():

            return

        self.peek()

        self.dequeue()

        return self.print()
