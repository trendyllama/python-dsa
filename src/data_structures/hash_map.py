"""
- contains doubly linked list class
"""

from typing import Any, Hashable, Optional
from .node import Node
from .linked_list import LinkedList


class HashMap:
    """
    - codecademy implementation of a hashmap
    """

    def __init__(self, size: int) -> None:
        """_summary_

        Args:
            size (int): _description_
        """
        self.array_size = size
        self.array: list = [LinkedList() for _ in range(self.array_size)]

    def hash(self, key: Hashable) -> int:
        """_summary_

        Args:
            key (Hashable): _description_

        Returns:
            int: _description_
        """
        hash_code = hash(key)
        return hash_code

    def compress(self, hash_code):
        """_summary_

        Args:
            hash_code (bool): _description_

        Returns:
            _type_: _description_
        """
        return hash_code % self.array_size

    def assign(self, key: Hashable, value: Any) -> None:
        """_summary_

        Args:
            key (Hashable): _description_
            value (Any): _description_
        """
        payload = Node([key, value])
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        list_at_array = self.array[array_index]

        for i in list_at_array:
            if i[0] == key:
                i[1] = value

        list_at_array.insert(payload)

    def retrieve(self, key: Hashable) -> Optional[list]:
        """_summary_

        Args:
            key (Hashable): _description_

        Returns:
            Optional[list]: _description_
        """
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        payload: list = self.array[array_index]
        list_at_index = Node([array_index, payload])

        if payload[0] == key:
            return payload[1]

        if payload is None or payload[0] != key:
            return None

        for i in list_at_index:
            if i[0] == key:
                return i[1]
            else:
                return None
