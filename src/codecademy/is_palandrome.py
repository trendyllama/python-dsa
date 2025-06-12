
def is_palindrome_r(str):
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome_r(str[1:-1])


def is_palindrome_i(my_string):
    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True


# test cases
def test_is_palindrome():
    assert is_palindrome_i("abba")
    assert is_palindrome_i("abcba")
    assert is_palindrome_i("")
    assert is_palindrome_i("abcd") is False
