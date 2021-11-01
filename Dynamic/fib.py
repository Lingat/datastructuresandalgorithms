def fib(n, arr):
    if arr[n] != None:
        return arr[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, arr) + fib(n - 2, arr)
    arr[n] = result
    return result


arr = 500 * [None]
for i in range(1, 11):
    print("|" * fib(i, arr))
