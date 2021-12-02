'''
You’re given an array of n integers, and must answer a series of n queries, each
of the form: “how many elements of the array have value between L and R?”,
where L and R are integers. Design an O(n log n) algorithm that answers all
of these queries.

1) Sort the array, this will take O(n log n) time
2) Use binary search to find the low and high, count the in between 
3) Return the answer

'''
def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1
        
def countBetween(arr, L, R):
    arr.sort()
    length = len(arr)
    low = arr[0]
    high = arr[len(arr)-1]

    if(L > high or R < low):
        return 0
    
    i = 0 
    while i < length:
        if()

        i+=1