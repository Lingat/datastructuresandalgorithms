def insertionSort(arr):

    '''
    Correct insertion sort
    '''
    # example array [4, 3, 2, 1]
    for i in range(1, len(arr)):
        print()
        print("ITERATION {}".format(i))
        # FIRST ITERATION: arr[1], curr = 3
        curr = arr[i] 
        print("arr: {}".format(arr))
        print("Curr: {}".format(curr))
        j = i-1

        print("j: {}".format(j))
        # FIRST ITERATION: j = 0
        # don't run if j is less than 0 (-1 is not an index)
        # or if the current element is less than j-th position in arr
        
        # FIRST ITERATION: arr[j], arr[0] = 4
        # FIRST ITERATION: j >= 0 is true and 3 < 4
        while j >= 0 and curr < arr[j]:
            arr[j + 1]  = arr[j] 
            print()
            print("j: {}".format(j))
            print("arr[{}] = arr[{}]".format(j+1, j))
            print("arr = {}".format(arr))
            print()
            # FIRST ITERATION: arr[1] = arr[0]
            # FIRST ITERATION: arr = [4, 4, 2, 1]

            j -= 1
            # FIRST ITERATION: j = -1, j < 0 so exit loop

 
        arr[j + 1] = curr
        print("arr[{}] = {}".format(j+1, curr))
        print("arr = {}".format(arr))
         # FIRST ITERATION: arr[0] = 3
         # FIRST ITERATION: arr = [3, 4, 2, 1]

    '''
    My incorrect insertion sort
    sorted_arr = []
    for n in arr:
        if(len(sorted_arr) == 0):
            sorted_arr.append(n)
            continue

        inserted = False
        if(n <= sorted_arr[0]):
            sorted_arr.insert(0, n)
            inserted = True
        if(not inserted):
            for j in range(len(sorted_arr)):
                if(j!=len(sorted_arr) - 1 and n >= sorted_arr[j] and n<=sorted_arr[j+1]):
                    sorted_arr.insert(j+1, n)
                    inserted = True
                    break
        if(not inserted):
            sorted_arr.append(n)
    return sorted_arr
    '''
    return arr

array = [4, 3, 2, 1]
print("Unsorted: {}".format(array))
print("Sorted: {}".format(insertionSort(array)))