def pattern_search(text: str, pattern: str) -> None:
    """
    - string pattern searching algo
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


TEXT = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
PATTERN = "NEEDLE"
pattern_search(TEXT, PATTERN)
