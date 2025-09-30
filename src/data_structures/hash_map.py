"""
- contains doubly linked list class
"""

import logging
from collections.abc import Hashable

from .linked_list import LinkedList
from .node import Node

logger = logging.getLogger(__name__)

class HashMap:
    """
    - codecademy implementation of a hashmap
    """

    def __init__(self, size: int) -> None:
        logger.debug("Initializing HashMap with size %s", size)
        self._array_size = size

    @property
    def array_size(self) -> int:
        logger.debug("Getting array size: %s", self._array_size)
        return self._array_size

    @property
    def array(self) -> list:
        return [LinkedList() for _ in range(self.array_size)]

    def hash(self, key: Hashable) -> int:
        hash_code = hash(key)
        logger.debug("Hash code for key %s: %s", key, hash_code)
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
        logger.debug("Hash code for key %s: %s", key, hash_code)
        array_index = self.compress(hash_code)
        logger.debug("Array index for key %s: %s", key, array_index)
        payload: list = self.array[array_index]
        list_at_index = Node([array_index, payload])

        if payload[0] == key:
            logger.debug("Key found: %s", key)
            logger.debug("Value: %s", payload[1])
            return payload[1]

        if payload is None or payload[0] != key:
            return None

        for i in list_at_index:
            logger.debug("Checking key: %s", i[0])
            if i[0] == key:
                return i[1]
            else:
                return None
