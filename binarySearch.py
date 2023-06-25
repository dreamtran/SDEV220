import random


def binarySearch(arr, search_number):
    low = 0
    high = len(arr) - 1
    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] < search_number:
            low = mid + 1
        else:
            high = mid

    if arr[low] == search_number:
        print('Index:', low)
    elif arr[high] == search_number:
        print('Index:', high)
    else:
        print("Not found")

arr = [2, 3, 4, 10, 40]
x=10
binarySearch(arr, x)
