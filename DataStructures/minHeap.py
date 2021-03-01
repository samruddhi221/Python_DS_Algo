# reference: https://medium.com/swlh/data-structures-heaps-b039868a521b
# Heaps are used when the highest or lowest order/priority element needs
# to be removed.Heaps are used when the highest or lowest order/priority
# element needs to be removed.Heaps are used when the highest or lowest
# order/priority element needs to be removed.Heaps are used when the highest
# or lowest order/priority element needs to be removed.Heaps are used when
# the highest or lowest order/priority element needs to be removed.
#
# If we are looking at the i-th index in an array:
# It’s parent is at the floor (i-1)/2 index.
# It’s left child is at 2 * i + 1 index.
# It’s right child is at 2 *i + 2 index.
# Implementation of Max_Heap is similar.

class MinHeap:
    def __init__(self, array: list):
        self.heap_array = array

    def heapify(self, index: int) -> None:
        size = len(self.heap_array)
        index_smallest = index
        index_left_child = 2 * index + 1
        index_right_child = 2 * index + 2

        if index_left_child < size and self.heap_array[index_smallest] > self.heap_array[index_left_child]:
            index_smallest = index_left_child

        if index_right_child < size and self.heap_array[index_smallest] > self.heap_array[index_right_child]:
            index_smallest = index_right_child

        if index_smallest != index:
            self.heap_array[index_smallest], self.heap_array[index] = self.heap_array[index], self.heap_array[index_smallest]
            self.heapify(index_smallest)
        return

    def get_min(self):
        return self.heap_array[0]

    def heap_pop(self):
        if len(self.heap_array) == 0:
            return
        elif len(self.heap_array) == 1:
            self.heap_array.pop()
        else:
            self.heap_array[0], self.heap_array[-1] = self.heap_array[-1], self.heap_array[0]
            self.heap_array.pop()
            for i in range((len(self.heap_array)-1)//2, -1, -1):
                self.heapify(i)

    def heap_push(self, value: int) -> None:
        # first element
        if len(self.heap_array) == 0:
            self.heap_array.append(value)
        # rest of the elements
        else:
            self.heap_array.append(value)
            size = len(self.heap_array)
            for i in range((size - 1) // 2, -1, -1):
                self.heapify(i)  # i: index of smallest element in current subtree

    def min_heapify(self):
        for i in range((len(self.heap_array)-1)//2, -1, -1):
            self.heapify(i)


if __name__ == '__main__':
    arr = []
    min_heap = MinHeap(arr)
    min_heap.heap_push(3)
    min_heap.heap_push(1)
    min_heap.heap_push(6)
    min_heap.heap_push(2)
    min_heap.heap_push(5)
    min_heap.heap_push(4)
    print(arr)
    min_heap.heap_pop()
    print(arr)
    min_heap.heap_pop()
    print(arr)
    arr2 = [9, 8, 7, 11, 10, 18]
    print(arr2)
    min_heap2 = MinHeap(arr2)
    min_heap2.min_heapify()
    print(arr2)