"""

The factory is a creational design pattern we can use to create concrete implementations of an interface.

This pattern is useful for eliminating complex conditional statements when creating objects.
It allows us to create objects without specifying the exact class of object that will be created.
"""

from typing import Protocol
import json


class File(Protocol):
    def read(self) -> str: ...

    def write(self, data: str) -> None: ...


class FileParserFactory:
    """
    implement methods for each file type

    these methods will be used to parse the file behind
    a generic parse method

    """

    def _parse_json(self, file: File) -> str:
        with open(file.read(), "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    def _parse_xml(self, file: File) -> str:
        raise NotImplementedError("XML parsing is not implemented yet")

    def _parse_yaml(self, file: File) -> str:
        raise NotImplementedError("YAML parsing is not implemented yet")

    def parse(self, file: File, file_type: str) -> str:
        """
        generic parse method that can be extended to support other file types

        hides these if statements from behind a clean interface
        """
        if file_type == "json":
            return self._parse_json(file)

        if file_type == "xml":
            return self._parse_xml(file)

        if file_type == "yaml":
            return self._parse_yaml(file)

        raise ValueError(f"Unsupported file type: {file_type}")


def file_parser(file: File, file_type: str) -> str:
    """
    factory method that creates a FileParserFactory instance
    and calls the parse method on it

    hides the complexity of creating a FileParserFactory instance
    """
    factory = FileParserFactory()
    return factory.parse(file, file_type)
