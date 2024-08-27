from typing import Optional, Any
from .node import Node


class StackOverflowError(Exception):
    """
    - exception for handling a stack overflow
    """


class EmptyStackError(Exception):
    """
    - exception for handling an empty stack
    """


class Stack:
    """
    - codecademy implementation of a stack
    """

    def __init__(self) -> None:
        self.size: int = 0
        self.top_item: Optional[Node] = None
        self.limit: int = 1000

    def push(self, value: Any) -> None:
        """
        - adds a node to the top of the stack
        """

        if self.has_space():
            item = Node(value)

            if not isinstance(self.top_item, Node):
                raise EmptyStackError

            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1

        else:
            raise StackOverflowError

    def pop(self) -> None:
        """
        - removes the top node of the stack
        """

        if self.size > 0:

            item_to_remove = self.top_item

            if not isinstance(item_to_remove, Node):
                raise EmptyStackError

            self.top_item = item_to_remove.get_next_node()
            self.size -= 1

        else:
            raise EmptyStackError

    def peek(self) -> Any:
        """
        - returns the value of the Node at the top of the stack
        """

        if self.size > 0:

            if not isinstance(self.top_item, Node):
                raise EmptyStackError

            return self.top_item.get_value()

        raise EmptyStackError

    def has_space(self) -> bool:
        return self.limit > self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def print_items(self) -> None:

        if not isinstance(self.top_item, Node):
            raise EmptyStackError

        pointer = self.top_item
        print_list: list[Node] = []

        while pointer:
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print(f"Stack: {print_list}")

        return
