'''
connections example:
    [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]


'''

from typing import Self, Any
from src.data_structures.node import Node



class Connection:

    def __init__(self, *args: Node) -> None:

        if len(args) != 2:
            raise ValueError

        self.connection = (arg for arg in args)

class Graph:

    connections: list[Connection]


    def add_connection(self, connection: Connection) -> Self:

        self.connections.append(connection)

        return self

    def add(self, *args: Node) -> Self: ...


    def remove(self, node: Node) -> Self: ...
