def merge(left: list, right: list, result: list) -> None:
    n_left = len(left)
    n_right = len(right)
    index_left, index_right, index_result = 0, 0, 0

    while index_left < n_left and index_right < n_right:
        if left[index_left] <= right[index_right]:
            result[index_result] = left[index_left]
            index_left += 1
        else:
            result[index_result] = right[index_right]
            index_right += 1
        index_result += 1

    # for extra remaining elements, unless one of the left or right parts are done adding, loop above won't exit
    # Only one of the following two will be executed
    while index_left < n_left:
        result[index_result] = left[index_left]
        index_left += 1
        index_result += 1
    while index_right < n_right:
        result[index_result] = right[index_right]
        index_right += 1
        index_result += 1


def merge_sort(array_to_sort: list) -> list:
    if len(array_to_sort) < 2:
        return array_to_sort

    # split the array in left and right part
    mid = len(array_to_sort) // 2
    left = array_to_sort[0:mid]
    right = array_to_sort[mid:]
    merge_sort(left)
    merge_sort(right)

    merge(left, right, array_to_sort)
    return array_to_sort


if __name__ == "__main__":
    array = [3, 6, 0, 4, 10, 5, 4, 2]
    print("Original Array:", array)
    sorted_array = merge_sort(array)
    print("Sorted Array:", sorted_array)
