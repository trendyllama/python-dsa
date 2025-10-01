from typing import Protocol


class IPatternSearcher(Protocol):
    pattern: str

    def search(self) -> tuple[int, str]: ...


def pattern_search(text: str, pattern: str) -> tuple[int, str] | None:
    """
    - string pattern searching algo

    Examples:
    >>> pattern_search("HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE", "NEEDLE")
    (6, 'NEEDLE')
    >>> pattern_search("HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE", "NEEDLEHAY")
    (6, 'NEEDLEHAY')
    """
    for index, _ in enumerate(text):
        match_count = 0
        for char, _ in enumerate(pattern):
            if pattern[char] == text[char + index]:
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            return (index, pattern)


def find_pattern(text: str, pattern: str) -> bool:
    """
    - string pattern searching algo

    Examples:
    >>> find_pattern("HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE", "NEEDLE")
    True
    >>> find_pattern("HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE", "NEEDLES")
    False

    """

    return pattern in text


def find_number_of_patterns(text: str, pattern: str) -> int:
    """
    - string pattern searching algo

    """

    raise NotImplementedError
