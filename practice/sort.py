def bubble_sort(array):
    size = len(array)
    for i in range(size):
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        min_index = i
        for j in range(size - i):
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def insertion_sort(array):
    size = len(array)
    for i in range(1, size):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1
    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1
    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = (0 + len(array)) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    return merge(merge_sort(left_array), merge_sort(right_array))


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    lesser, equal, greater = [], [], []

    for num in array:
        if num < pivot:
            lesser.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return quick_sort(lesser) + equal + quick_sort(greater)


if __name__ == '__main__':
    new_array = quick_sort([5, 12, 4, 2, 1])
    print(new_array)
