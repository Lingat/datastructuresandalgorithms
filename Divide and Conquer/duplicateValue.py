
import sys


def duplicateValue(arr):
    arr2 = []
    for i in range(len(arr)):
        if(not arr[i] in arr2):
            arr2.append(arr[i])
        else:
            return arr[i]
    return -1


arr = sys.argv[1].split(',')

for i in range(len(arr)):
    arr[i] = int(arr[i])

print(duplicateValue(arr))
