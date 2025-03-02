from typing import Callable, Optional, Self, Union, Any

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

    def enqueue(self, value) -> Self:
        self._increase_size()

        match self.is_empty:
            case True:
                new_node = Node(value, None, None)

                self.head = new_node

                self.tail = new_node

            case False:
                new_node = Node(value, self.tail, None)

                self.tail = new_node

        return self

    def dequeue(self) -> Self:
        match self.is_empty:
            case True:
                raise EmptyQueueError("Cannot dequeue from an empty queue")

            case False:
                assert self.head is not None
                self.head = self.head.previous_node
                self._decrease_size()

                if self.head is None:
                    self.tail = None

        return self

    def peek(self) -> Any:
        if self.head is None:
            raise EmptyQueueError("Cannot peek from an empty queue")

        return self.head.value

    def print(self) -> Union[Callable, Self]:
        # TODO: this isnt working

        match self.head:
            case Node():
                self.peek()
                self.head = self.head.previous_node
                return self.print()

            case None:
                return self

    def __iter__(self) -> Self:
        self.current_node = self.head

        return self

    def __next__(self) -> Any:
        if self.current_node is None:
            raise StopIteration

        value = self.current_node.value

        self.current_node = self.current_node.previous_node

        return value
