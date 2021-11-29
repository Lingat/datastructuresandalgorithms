def gridTraveler(n, m, arr={}):
    if n in arr and m in arr[n]:
        return arr[n][m]
    elif n == 1 and m == 1:
        return 1
    elif n == 0 or m == 0:
        return 0

    arr[n] = {}
    arr[n][m] = gridTraveler(n-1, m, arr) + gridTraveler(n, m-1, arr)
    return arr[n][m]


print(gridTraveler(18, 18))
