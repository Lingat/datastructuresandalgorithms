def insertionSort(arr):
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

print(insertionSort([123, 3243234, 1, 0, -1, 123, 22222, 4, 2, 3]))