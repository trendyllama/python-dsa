"""
- contains linked list class
"""

from src.data_structures.node import Node


class LinkedList:
    """
    - codecademy implementation of linked list
    """

    def __init__(self, head_node: Node | None = None) -> None:
        self._head_node = head_node

    @property
    def head_node(self) -> Node | None:
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
