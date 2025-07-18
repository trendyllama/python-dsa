from functools import reduce
import random


def larger_sum(lst1: list[int], lst2: list[int]) -> tuple[int, list[int], int]:
    sum1 = reduce(lambda x, y: x + y, lst1)

    sum2 = reduce(lambda x, y: x + y, lst2)

    return (
        1 if sum1 > sum2 else 2,
        lst1 if sum1 > sum2 else lst2,
        sum1 if sum1 > sum2 else sum2,
    )


if __name__ == "__main__":
    lst_first = list(map(lambda _: random.randint(0, 1000), range(200)))
    lst_second = list(map(lambda _: random.randint(0, 1000), range(200)))
    print(larger_sum(lst_first, lst_second))
