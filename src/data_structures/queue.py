from typing import Callable, Optional, Self, Union

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
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return bool(self.head is None and self.tail is None)

    def increase_size(self) -> Self:
        self.size += 1

        return self

    def decrease_size(self) -> Self:
        self.size -= 1

        return self

    def enqueue(self, value) -> Self:

        self.increase_size()

        match self.is_empty():

            case True:

                new_node = Node(value, None, None)

                self.head = new_node

                self.tail = new_node

            case False:

                new_node = Node(value, self.tail, None)

                self.tail = new_node

        return self


    def dequeue(self) -> Self:

        self.decrease_size()

        match self.is_empty():

            case True:
                raise EmptyQueueError("Cannot dequeue from an empty queue")

            case False:
                assert self.head is not None

                self.head = self.head.get_prev_node()

        return self


    def peek(self) -> Self:

        if self.head is None:
            raise TypeError

        print(self.head.value)

        return self

    def print(self) -> Union[Callable, Self]:
        """_summary_

        Returns:
            Optional[Callable]: _description_
        """

        # TODO: this isnt working

        if not isinstance(self.head, Node):
            return Self

        self.peek()

        self.head = self.head.get_prev_node()

        return self.print()
