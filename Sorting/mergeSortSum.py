
sumFound = False
def mergeSortSum(arr, x):
    global sumFound
    if(sumFound):
        return True
        
    if len(arr) > 1:
        half = len(arr) // 2 # half the array

        # split
        L = arr[half:]
        R = arr[:half]  


        mergeSortSum(L, x)
        mergeSortSum(R, x)
       
        i = j = k = 0

        # check at point of merge
        while i < len(L) and j < len(R):
     
            sumOfElements = L[i] + R[j]
            if sumOfElements == x:
                sumFound = True
                print(L[i], R[j])
          

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
        return sumFound
  




print(mergeSortSum([0, 0, 0, 0, 5, 123, 123, 99], 100))