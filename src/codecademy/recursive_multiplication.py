from functools import cache


@cache
def multiplication(n, m):
    # base case
    if n == 0 or m == 0:
        return 0
    return n + multiplication(n, m - 1)

@cache
def recursive_sum(n: int, m: int) -> int:

    if n == 0:
        return m

    return recursive_sum(n - 1, m + 1)

# test cases

assert multiplication(3, 7) == 21
assert multiplication(5, 5) == 25
assert multiplication(0, 4) == 0


assert recursive_sum(1, 2) == 3
assert recursive_sum(5, 7) == 12
assert recursive_sum(30, 12) == 42