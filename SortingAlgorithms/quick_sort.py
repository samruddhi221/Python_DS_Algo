def partition(array, start, end) -> int:
    """
    Divides the array into left and right parts where left part has elements less that pivot and
    right part has elements more than pivot.
    :param array: complete array (last element of the array is selected as a pivot element)
    :param start: start index
    :param end: end index
    :return: index of current pivot element in the array
    """
    pivot = array[end]
    pivot_index = start
    for i in range(start, end+1):
        if array[i] < pivot:
            array[pivot_index], array[i] = array[i], array[pivot_index]
            pivot_index += 1
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return pivot_index


def quick_sort(array, start, end) -> None:
    """
    In place quick sort: time complexity O(n*log n), space complexity:O(1)
    :param array: original array
    :param start: start index of current partition
    :param end: end index of the current partition
    :return: None
    """
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)


if __name__ == "__main__":
    array = [3, 6, 0, 4, 10, 5, 4, 2]
    print("Original Array:", array)
    quick_sort(array, 0, len(array) - 1)
    print("Sorted Array:", array)
