''' 
    N robbers with N items. 
    1) Keep a count of the items being given out
    2) Sort the items and robbers according to their values
    3) Starting from the lowest, select the item if the first robber wants it, keep track of all the items given out
    4) if count != N, then we know there is no fair distribution
'''


def canDistribute(robbers, items):

    N = len(robbers)
    items.sort()
    robbers.sort()
    i = 0
    count = 0
    a = False
    for j in range(N):
        if(items[j] >= robbers[i]):
            i = j+1
            count += 1

    if(count >= N):
        return True
    return False


robbers = [5000, 1, 2, 3]
items = [100, 51, 223, 323]
x = canDistribute(robbers, items)

print(f"robbers: {robbers}")
print(f"items: {items}")
print(f"canDistribute: {x}")
