import queue


class stack(object):
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, value):
        self.q1.put(value)

    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return self.q2.get()


class customQueue(object):
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def enqueue(self, value):
        self.first_stack.append(value)

    def dequeue(self):
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()


def quick_sort(array):
    less_array, equal_array, grater_array = [], [], []
    size = len(array)

    if size <=1:
        return
    pivote = array[size // 2]

    for i in array:
        if i < pivote:
            less_array.append(i)
        elif i == pivote:
            equal_array.append(i)
        else:
            grater_array.append(i)

    return quick_sort(less_array) + equal_array + quick_sort(grater_array)


def merge(array1,array2):
    result = []
    array_index1 = 0
    array_index2 = 0

    while array_index1 < len(array1) and array_index2 < len(array2):
        if array1[array_index1] < array2[array_index2]:
            result.append(array1[array_index1])
            array_index1 += 1
        else:
            result.append(array2[array_index2])
            array_index2 += 1

    if array_index1 == len(array1):
        while array_index2 < len(array2):
            result.append(array2[array_index2])
            array_index2 += 1
    if array_index2 == len(array2):
        while array_index1 < len(array1):
            result.append(array1[array_index1])
            array_index1 += 1
    return result


def merge_sort(array):
    size = len(array)

    if size <= 1:
        return array

    mid = size // 2

    left_array = array[:mid]
    right_array = array[mid:]

    return merge(merge_sort(left_array),merge_sort(right_array))
