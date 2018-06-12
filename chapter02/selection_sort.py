def find_smallest_index(arr):
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    arr_result = []
    for i in range(len(arr)):
        smallest_index = find_smallest_index(arr)
        arr_result.append(arr.pop(smallest_index))
    return arr_result


if __name__ == '__main__':
    arr = [11, 80, 5, 4, 324, 3431]
    print(selection_sort(arr))
