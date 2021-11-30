def bestSum(n, arr, sumArr = [], memo={}):
    arr.sort(reverse=True)
    if(n in memo):
        return memo[n]
    if(n == 0):
        return []
    if(n < 0):
        return None

    shortestComb = None

    for num in arr:
        remainder = n - num
        remainderComb = bestSum(remainder, arr, sumArr, memo)

        if(remainderComb != None):
            comb = []
            for i in remainderComb:
                comb.append(i)
            comb.append(num)
            if(shortestComb == None or len(comb) < len(shortestComb)):
                shortestComb = comb
           
          
    memo[n] = shortestComb
    return shortestComb


print(bestSum(7, [5, 3, 4, 7], [], {}))
print(bestSum(8, [2, 3, 5], [], {}))
print(bestSum(8, [1, 4, 5], [], {}))
print(bestSum(100, [1, 2, 5, 25], [], {}))
