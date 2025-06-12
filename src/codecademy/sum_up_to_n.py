from functools import cache, reduce

@cache
def sum_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n - 1)


def sum_to_n_functional(n: int) -> int:

    zero_to_n_range = range(0, n + 1)

    sum_out = reduce(lambda x, y: x + y, zero_to_n_range)

    return sum_out



assert sum_to_n(4) == 10
assert sum_to_n(5) == 15
assert sum_to_n(20) == 210
assert sum_to_n(100) == 5050


assert sum_to_n_functional(4) == 10
assert sum_to_n_functional(100) == 5050