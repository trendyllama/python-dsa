from src.data_structures.node import Node
from typing import Optional, Callable


class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self) -> None:

        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:

        return bool(self.head is None and self.tail is None)


    def enqueue(self, value) -> None:

        match self.is_empty():

            case True:

                new_node = Node(value, None, None)
                self.size += 1
                self.head = new_node

                self.tail = new_node

            case False:

                new_node = Node(value, self.tail, None)

                self.size += 1
                self.tail = new_node


    def dequeue(self) -> None:

        self.size -= 1

        match self.is_empty():

            case True:
                raise EmptyQueueError("Cannot dequeue from an empty queue")

            case False:

                self.head = self.head.get_prev_node()



    def peek(self) -> None:

        print(self.head.value)


    def print(self) -> Optional[Callable]:

        match self.is_empty():

            case True:
                return

            case False:
                self.peek()

                self.dequeue()

                return self.print()
