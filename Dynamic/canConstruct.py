'''
Write a function canConstruct that accepts a target string
and an array of strings. 

The function should return a boolean indicating whether or not the
'target' can be constructed by cocatenating elements of the wordBank
array

You may reuse elements of wordBank as many times as needed

Steps (Brute Force)
Base Case: 
target is empty, return True

1) find if string at wordBank[i] is in target
2) if in target, take it away from target and recursively call function
3) continue until no words from wordBank are in target or target is empty

m is target length
n is wordBank length
Complexity: O(n^m*m)
Space: O(m^2)


Steps (Optimised)
Base Case: 
target is empty, return True

1) find if target is in memo, if it is return wordBank[i]
2) otherwise, continue using brute force steps

m is target length
n is wordBank length
Complexity: O(n*m^2)
Space: O(m^2)
'''

def canConstruct(target, wordBank, memo={}):
    if(target in memo):
        return memo[target]
    if(len(target) == 0):
        return True
    
    for word in wordBank:
        if(word in target):
            memo[target] = canConstruct(target.replace(word, ''), wordBank)
            return canConstruct(target.replace(word, ''), wordBank)

    memo[target] = False
    return False


print(canConstruct("eeeeeeeeee", ["123", "456", "11111111"]))
