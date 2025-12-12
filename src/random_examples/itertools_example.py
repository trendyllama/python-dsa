import sys
from itertools import batched, chain, groupby, islice, tee


def example_groupby():
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30},
    ]

    # Group by age
    grouped = groupby(data, key=lambda x: x["age"])
    for age, group in grouped:

        sys.stdout.write(f"Age: {age}\n")
        for person in group:
            sys.stdout.write(f" - {person['name']}\n")


def example_chain():
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    combined = chain(list1, list2)
    sys.stdout.write(str(list(combined)) + "\n")

def example_batched():
    data = range(10)
    batched_data = batched(data, 3)
    for batch in batched_data:
        sys.stdout.write(str(batch) + "\n")


def example_islice():
    data = range(10)
    sliced = islice(data, 2, 8, 2)
    sys.stdout.write(str(list(sliced)) + "\n")


def example_tee():
    data = range(5)
    iter1, iter2 = tee(data, 2)
    sys.stdout.write("Iterator 1: " + str(list(iter1)) + "\n")
    sys.stdout.write("Iterator 2: " + str(list(iter2)) + "\n")

if __name__ == "__main__":
    example_groupby()
    example_chain()
    sys.stdout.flush()
