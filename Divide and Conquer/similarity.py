import random
import sys


def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return True

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return False


def hasSimilarity(arr1, arr2):
    arr1.sort()

    for i in range(len(arr2)):
        if(binarySearch(arr1, 0, len(arr1)-1, arr2[i])):
            return True
    return False


arr1 = sys.argv[1].split(',')

for i in range(len(arr1)):
    arr1[i] = int(arr1[i])

arr2 = []

for i in range(len(arr1)):
    arr2.append(random.randint(1, 9))

print(f"Arr1: {arr1}")
print(f"Arr2: {arr2}")

x = hasSimilarity(arr1, arr2)
print(f"Similarities: {x}")
