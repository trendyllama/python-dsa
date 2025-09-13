"""

The factory is a creational design pattern we can use to create concrete implementations of an interface.

This pattern is useful for eliminating complex conditional statements when creating objects.
It allows us to create objects without specifying the exact class of object that will be created.
"""

import json
from pathlib import Path
from typing import Protocol


class File(Protocol):
    def read(self) -> Path: ...

    def write(self, data: str) -> None: ...


class FileParserFactory:
    """
    implement methods for each file type

    these methods will be used to parse the file behind
    a generic parse method

    """

    def _parse_json(self, file: File) -> str:

        data = json.loads(file.read().read_text())

        return data

    def _parse_xml(self, file: File) -> str:
        msg = "XML parsing is not implemented yet"
        raise NotImplementedError(msg)

    def _parse_yaml(self, file: File) -> str:
        msg = "YAML parsing is not implemented yet"
        raise NotImplementedError(msg)

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

        msg = f"Unsupported file type: {file_type}"
        raise ValueError(msg)


def file_parser(file: File, file_type: str) -> str:
    """
    factory method that creates a FileParserFactory instance
    and calls the parse method on it

    hides the complexity of creating a FileParserFactory instance
    """
    return FileParserFactory().parse(file, file_type)
