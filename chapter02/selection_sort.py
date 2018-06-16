import random

from common.log_time import log_time


def find_smallest_index(arr):
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return smallest_index


@log_time
def selection_sort(arr):
    arr_result = []
    for i in range(len(arr)):
        smallest_index = find_smallest_index(arr)
        arr_result.append(arr.pop(smallest_index))
    return arr_result


if __name__ == '__main__':
    nums = [x for x in range(10000, 0, -1)]
    random.shuffle(nums)
    selection_sort(nums)

    nums = [x for x in range(10000)]
    random.shuffle(nums)
    selection_sort(nums)
