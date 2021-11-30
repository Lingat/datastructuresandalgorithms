'''
Write a function countConstruct that accepts a target string
and an array of strings. 

The function should return the number of ways that the 'target' can be
constructed by concatenating elements of the wordBank array

You may reuse elements of wordBank as many times as needed

Steps (Brute Force)
Base Case: 
target is empty, return 1 


1) Iterate through wordBank, check if wordBank[i] is in target
2) if it is, recursively call the function, slicing wordBank[i] from target and 
input that as the new target
3) Continue until target is empty or there are no words in wordBank in target

m = target.length
n = wordBank.length

Time Complexity: O(n^m * m)
Space: O(m^2)

With memo -->
Time Complexity: O(n^m^2)
Space: O(m^2)

'''

def countConstruct(target, wordBank, memo={}):
    if(target in memo):
        return memo[target]
    if(len(target) == 0):
        return 1
    
    
    count = 0
    for word in wordBank:
        if(word in target):
            num = countConstruct(target.replace(word, ''), wordBank)
            count+=num

    memo[target] = count
    return count


print(countConstruct("eeeeeeee", ["e", "eeee", "eeeeeeee", "eeeeeeee"]))
