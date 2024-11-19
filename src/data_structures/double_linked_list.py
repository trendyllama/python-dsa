from typing import Any

from .node import Node


class DoublyLinkedList:
    """
    - codecademy implementation of a doubly linked list
    """

    def __init__(self) -> None:
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value: Any) -> None:
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        match self.tail_node:
            case None:
                self.tail_node = new_head
            case _:
                return

    def add_to_tail(self, new_value: Any) -> None:
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self) -> None:
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_node()

        if self.head_node is not None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.get_prev_node()

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove: Any) -> None:
        node_to_remove = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        match node_to_remove:
            case None:
                return None

            case self.head_node:
                self.remove_head()

            case self.tail_node:
                self.remove_tail()

            case _:
                next_node = node_to_remove.get_next_node()

        if not isinstance(next_node, Node):
            raise TypeError

        prev_node = node_to_remove.get_prev_node()
        next_node.set_prev_node(prev_node)
        prev_node.set_next_node(next_node)

        return node_to_remove

    def stringify_list(self) -> str:
        string_list = ""
        current_node = self.head_node
        while current_node is not None:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
