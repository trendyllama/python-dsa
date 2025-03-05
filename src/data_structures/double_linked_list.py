
from .node import Node


class DoublyLinkedList:
    """
    - codecademy implementation of a doubly linked list
    """

    def __init__(self) -> None:
        self._head_node = None
        self._tail_node = None

    @property
    def head(self) -> Node | None:
        return self._head_node

    @head.setter
    def head(self, new_head: Node | None) -> None:
        self._head_node = new_head

    @property
    def tail(self) -> Node | None:
        return self._tail_node

    @tail.setter
    def tail(self, new_tail: Node | None) -> None:
        self._tail_node = new_tail

    def add_to_head(self, new_value) -> None:
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.previous_node = new_head
            new_head.next_node = current_head

        self.head_node = new_head

        match self.tail_node:
            case None:
                self.tail_node = new_head
            case _:
                return

    def add_to_tail(self, new_value) -> None:
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.next_node = new_tail
            new_tail.previous_node = current_tail

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self) -> None:
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.next_node

        if self.head_node is not None:
            self.head_node.previous_node = None

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.value

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.previous_node

        if self.tail_node is not None:
            self.tail_node.next_node = None

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.value

    def remove_by_value(self, value_to_remove) -> None:
        node_to_remove: Node | None = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.value == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.next_node

        match node_to_remove:
            case None:
                return None

            case self.head_node:
                self.remove_head()

            case self.tail_node:
                self.remove_tail()

            case _:
                next_node = node_to_remove.next_node

        if not isinstance(next_node, Node):
            raise TypeError

        prev_node = node_to_remove.previous_node
        next_node.previous_node = prev_node
        prev_node.next_node = next_node

        return node_to_remove

    def stringify_list(self) -> str:
        string_list = ""
        current_node = self.head_node
        while current_node is not None:
            if current_node.value is not None:
                string_list += str(current_node.value) + "\n"
            current_node = current_node.next_node
        return string_list

    def __iter__(self):
        self.current_node = self.head_node
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        value = self.current_node.value
        self.current_node = self.current_node.next_node
        return value

    def __str__(self) -> str:
        return self.stringify_list()

    def __repr__(self) -> str:
        return self.stringify_list()

    def __len__(self) -> int:
        current_node = self.head_node
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count
