def is_palindrome_r(input_string: str) -> bool:
    """
    Example:
    >>> is_palindrome_r("abba")
    True
    >>> is_palindrome_r("abcba")
    True
    >>> is_palindrome_r("")
    True
    >>> is_palindrome_r("abcd")
    False
    """

    if len(input_string) < 2:
        return True
    if input_string[0] != input_string[-1]:
        return False
    return is_palindrome_r(input_string[1:-1])


def is_palindrome_i(input_string: str) -> bool:
    """
    Example:
    >>> is_palindrome_i("abba")
    True
    >>> is_palindrome_i("abcba")
    True
    >>> is_palindrome_i("")
    True
    >>> is_palindrome_i("abcd")
    False
    """

    while len(input_string) > 1:
        if input_string[0] != input_string[-1]:
            return False
        input_string = input_string[1:-1]
    return True


def is_palandrome(input_string: str) -> bool:
    """
    Simplest Implementation

    Example:
    >>> is_palandrome("abba")
    True
    >>> is_palandrome("abcba")
    True
    >>> is_palandrome("")
    True
    >>> is_palandrome("abcd")
    False

    """

    return input_string == input_string[::-1]
