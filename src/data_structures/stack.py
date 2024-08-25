from typing import Optional, Any
from .node import Node


class Stack:
    def __init__(self, name = 'Test') -> None:
        self.size: int = 0
        self.top_item: Optional[Node] = None
        self.limit: int = 1000
        self.name: str = name

    def push(self, value) -> None:
        
        match self.has_space():
            case True:
                item = Node(value)
                item.set_next_node(self.top_item)
                self.top_item = item
                self.size += 1
            case False:
                print("No more room!")

    def pop(self) -> None:
        
        match self.size:
            case self.size if self.size > 0:
                item_to_remove = self.top_item
                self.top_item = item_to_remove.get_next_node()
                self.size -= 1
                return
            case _ :
                print("This stack is  empty.")
                return

    def peek(self) -> Any:
        
        match self.size:

            case self.size if self.size > 0:
                return self.top_item.get_value()
            case _ :
                print('the stack does not have a top value')
                return

    def has_space(self) -> bool:
        return self.limit > self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def get_name(self) -> int:
        return self.name

    def print_items(self) -> None:

        match isinstance(self.top_item, Node):
            case True:
                pointer = self.top_item
            case False:
                print("the stack is empty")
                return

        print_list: list[Node] = []

        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print(f"{self.get_name()} Stack: {print_list}")

        return
