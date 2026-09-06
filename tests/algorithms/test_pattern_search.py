import pytest

from src.algorithms.pattern_search import (
    find_number_of_patterns,
    find_pattern,
    pattern_search,
)


@pytest.mark.parametrize(
    ("text", "pattern", "expected"),
    [
        ("HAYHAYNEEDLE", "NEEDLE", (6, "NEEDLE")),
        ("NEEDLEHAY", "NEEDLEHAY", (0, "NEEDLEHAY")),
        ("HAYHAYHAY", "NEEDLE", None),
    ],
)
def test_pattern_search_returns_first_match(
    text: str, pattern: str, expected: tuple[int, str] | None
) -> None:
    assert pattern_search(text, pattern) == expected


@pytest.mark.parametrize(
    ("text", "pattern", "expected"),
    [
        ("HAYHAYNEEDLE", "NEEDLE", True),
        ("HAYHAYNEEDLE", "NEEDLES", False),
        ("", "NEEDLE", False),
    ],
)
def test_find_pattern_reports_whether_pattern_exists(
    text: str, pattern: str, expected: bool
) -> None:
    assert find_pattern(text, pattern) is expected


def test_find_number_of_patterns_is_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        find_number_of_patterns("HAYHAYNEEDLE", "HAY")
