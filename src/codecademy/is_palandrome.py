def is_palindrome_r(str: str) -> bool:
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

    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome_r(str[1:-1])


def is_palindrome_i(my_string: str) -> bool:
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

    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True
