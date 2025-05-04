def pattern_search(text: str, pattern: str) -> None:
    """
    - string pattern searching algo

    Examples:
    """
    print("Input Text:", text, "Input Pattern:", pattern)
    for index, _ in enumerate(text):
        print("Text Index:", index)
        match_count = 0
        for char, _ in enumerate(pattern):
            print("Pattern Index:", char)
            if pattern[char] == text[char + index]:
                print("Matching index found")
                print(f"Match count: {match_count}")

                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print(f"{pattern} found at index {index}")


def find_pattern(text: str, pattern: str) -> bool:
    """
    - string pattern searching algo

    Examples:
    >>> find_pattern("HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE", "NEEDLE")
    True
    >>> find_pattern("HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE", "NEEDLES")
    False

    """

    if pattern in text:
        return True
    return False


def find_number_of_patterns(text: str, pattern: str) -> int:
    """
    - string pattern searching algo

    """

    raise NotImplementedError
