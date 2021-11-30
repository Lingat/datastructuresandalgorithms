def howSum(n, arr, sumArr = [], memo={}):
    if(n in memo):
        return memo[n]
    if(n == 0):
        return sumArr
    if(n < 0):
        return None

    for num in arr:
        remainder = n - num
        if(howSum(remainder, arr, sumArr, memo) != None):
            sumArr.append(num)
            memo[n] = sumArr
            return sumArr

    memo[n] = None
    return None


print(howSum(98, [89, 14]))
