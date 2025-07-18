"""
- contains linked list class
"""

from src.data_structures.node import Node


class LinkedList:
    """
    - codecademy implementation of linked list
    """

    def __init__(self, head_node: Node | None = None) -> None:
        """
        - initializes a linked list as empty by default

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.head_node
        >>> linked_list.head_node = Node(1)
        >>> linked_list.head_node.value
        1
        """
        self._head_node = head_node

    @property
    def head_node(self) -> Node | None:
        """
        - returns the head node of the linked list

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.head_node
        >>> linked_list.head_node = Node(1)
        >>> linked_list.head_node.value
        1
        """
        return self._head_node

    @head_node.setter
    def head_node(self, new_head_node: Node | None) -> None:
        self._head_node = new_head_node

    @property
    def is_empty(self) -> bool:
        """
        - returns True if the linked list is empty

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.is_empty
        True
        >>> linked_list.append(1)
        >>> linked_list.is_empty
        False
        """
        return self.head_node is None

    def append(self, new_node_value) -> None:
        """
        - adds a new node to the end of the linked list
        - if the linked list is empty, it sets the new node as the head node

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> linked_list.head_node.value
        1
        """
        if self.is_empty:
            self.head_node = Node(new_node_value, None)
            return

        current_node = self.head_node

        while current_node is not None:
            if current_node.next_node is None:
                current_node.next_node = Node(new_node_value, None)
                return
            current_node = current_node.next_node

    def delete(self, value_to_delete) -> None:
        """
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> linked_list.delete(2)
        >>> linked_list.head_node.next_node.value
        3
        """
        if self.is_empty:
            return

        current_node = self.head_node

        while current_node is not None:
            if current_node.next_node is None:
                raise ValueError(f"Value {value_to_delete} not found in list")

            # want to look ahead by one node to see if the next node is the one to delete
            if current_node.next_node.value == value_to_delete:
                current_node.next_node = current_node.next_node.next_node
                return

            current_node = current_node.next_node

    def insert(self, new_node_value, index) -> None:
        """
        - inserts a new node at the given index
        - if the index is out of bounds, it raises an IndexError

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> linked_list.insert(4, 1)
        >>> linked_list.head_node.value
        1
        >>> linked_list.head_node.next_node.value
        4
        """
        if self.is_empty:
            raise IndexError("Index out of bounds")

        current_node = self.head_node
        current_index = 0

        for node in self:
            if current_node is None:
                raise IndexError("Index out of bounds")

            if current_index == index - 1:
                new_node = Node(new_node_value, current_node)
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return

            current_index += 1
            current_node = current_node.next_node

    def __str__(self) -> str:
        """
        - returns a string representation of the linked list

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> str(linked_list)
        '1 -> 2 -> 3'
        """
        if self.is_empty:
            return "Empty list"

        current_node = self.head_node
        result = ""

        while current_node is not None:
            result += str(current_node.value) + " -> "
            current_node = current_node.next_node

        return result[:-4]

    def __repr__(self) -> str:
        """
        - returns a string representation of the linked list

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> repr(linked_list)
        '1 -> 2 -> 3'
        """
        return self.__str__()

    def __len__(self) -> int:
        """
        - returns the length of the linked list

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> len(linked_list)
        3
        """
        if self.is_empty:
            return 0

        current_node = self.head_node
        count = 0

        while current_node is not None:
            count += 1
            current_node = current_node.next_node

        return count

    def __iter__(self):
        """
        - returns an iterator for the linked list
        - allows for iteration over the linked list
        - used in for loops
        - returns the value of the current node

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> iterator = iter(linked_list)
        >>> for value in iterator:
        ...     print(value)
        1
        2
        3
        """
        self.current_node = self.head_node
        return self

    def __next__(self):
        """
        - returns the next value in the linked list
        - raises StopIteration when the end of the linked list is reached

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.append(1)
        >>> linked_list.append(2)
        >>> linked_list.append(3)
        >>> iterator = iter(linked_list)
        >>> next(iterator)
        1
        >>> next(iterator)
        2
        >>> next(iterator)
        3
        """
        if self.current_node is None:
            raise StopIteration

        value = self.current_node.value
        self.current_node = self.current_node.next_node
        return value
