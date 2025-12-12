"""

The factory is a creational design pattern we can use to create concrete implementations of an interface.

This pattern is useful for eliminating complex conditional statements when creating objects.
It allows us to create objects without specifying the exact class of object that will be created.
"""

import json
from enum import StrEnum
from pathlib import Path
from typing import Protocol


class FileType(StrEnum):
    JSON = "json"
    XML = "xml"
    YAML = "yaml"

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

    def parse(self, file: File, file_type: FileType) -> str:
        """
        generic parse method that can be extended to support other file types

        hides these if statements from behind a clean interface
        """

        match file_type:
            case FileType.JSON:
                return self._parse_json(file)
            case FileType.XML:
                return self._parse_xml(file)
            case FileType.YAML:
                return self._parse_yaml(file)



def file_parser(file: File, file_type: FileType) -> str:
    """
    factory method that creates a FileParserFactory instance
    and calls the parse method on it

    hides the complexity of creating a FileParserFactory instance
    """
    return FileParserFactory().parse(file, file_type)
