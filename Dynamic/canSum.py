def canSum(n, arr, memo={}):
    if(n in memo):
        return memo[n]
    if(n == 0):
        return True
    if(n < 0):
        return False

    for num in arr:
        remainder = n - num
        if(canSum(remainder, arr, memo)):
            memo[n] = True
            return True

    memo[n] = False
    return False


print(canSum(14, [7, 14]))
