import math


def binarySearch(arr, x):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = math.floor(left + ((right - left) / 2))
        if(arr[mid] == x):
            return True
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


print(binarySearch([101, 20, 23, 3, 5], 100))
