def insertsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [2, 5, 1, 9, 6, 4]
insertsort(arr)
print(arr)


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


# def printarrray(array):
#     for i in range(len(array)):
#         print(array[i], end="")
#     print()


array = [12, 11, 13, 5, 6, 7]
print("original array is ", array)
mergeSort(array)
print("sorted array is")
print(array)
