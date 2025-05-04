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
    def array(self) -> list[LinkedList]:
        return list(map(lambda _: LinkedList(), range(self.array_size)))

    def hash(self, key: Hashable) -> int:
        hash_code = hash(key)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key: Hashable, value) -> None:
        '''

        - assigns a value to a key in the hashmap

        Examples:
        >>> hashmap = HashMap(10)
        >>> hashmap.assign('key1', 'value1')
        >>> hashmap.assign('key2', 'value2')
        >>> hashmap.assign('key3', 'value3')
        >>> hashmap.array[0].head_node.value
        ['key1', 'value1']
        >>> hashmap.array[1].head_node.value
        ['key2', 'value2']
        '''
        payload = Node([key, value])
        hash_code = self.hash(key)
        array_index = self.compress(hash_code)
        list_at_array = self.array[array_index]

        for i in list_at_array:
            if i is None:
                raise ValueError('Key not found')

            if i[0] == key:
                i[1] = value

        list_at_array.append(payload)

    def retrieve(self, key: Hashable) -> list | None:
        '''

        - retrieves the value associated with the key

        Examples:
        >>> hashmap = HashMap(10)
        >>> hashmap.assign('key1', 'value1')
        >>> hashmap.assign('key2', 'value2')
        >>> hashmap.retrieve('key1')
        'value1'
        >>> hashmap.retrieve('key2')
        'value2'
        >>> hashmap.retrieve('key3')
        >>> None
        '''
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
