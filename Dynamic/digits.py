def countEven(n, k):
    total = 0
    r = 0
    
    for i in range(10 ** (n-1), 10 ** (n)):
        digitCount = 0
        digitString = str(i)
        r+=1
        for j in digitString:
            if(int(j) == k):
                digitCount+=1

        if(digitCount % 2 == 0):
            total+=1
    # print(r)
    return total

n = 1
k = 2
print(countEven(n, k))


def testCount(n, k):
    total = 9 * (10**(n-1))
    for i in range(n-1):
        
    return total

print(testCount(n, k))
