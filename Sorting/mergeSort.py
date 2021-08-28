def mergeSort(arr):
    if len(arr) > 1:
        half = len(arr) // 2 # half the array

        # split
        L = arr[half:]
        R = arr[:half]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
                k+=1
            else:
                arr[k] = R[j]
                j+=1
                k+=1

        # checking if there's any numbers left
        while i < len(L): 
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R): 
            arr[k] = R[j]
            j+=1
            k+=1
  
