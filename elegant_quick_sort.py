def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    smaller = [x for x in array if x < pivot]
    larger = [x for x in array if x >= pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)
