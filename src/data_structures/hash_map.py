"""
- contains doubly linked list class
"""

from collections.abc import Hashable

from .linked_list import LinkedList
from .node import Node


class HashMap:
    """
    - codecademy implementation of a hashmap
    """

    def __init__(self, size: int) -> None:
        self._array_size = size

    @property
    def array_size(self) -> int:
        return self._array_size

    @property
    def array(self) -> list:
        return [LinkedList() for _ in range(self.array_size)]

    def hash(self, key: Hashable) -> int:
        hash_code = hash(key)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key: Hashable, value) -> None:
        payload = Node([key, value])
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        list_at_array = self.array[array_index]

        for i in list_at_array:
            if i[0] == key:
                i[1] = value

        list_at_array.insert(payload)

    def retrieve(self, key: Hashable) -> list | None:
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
