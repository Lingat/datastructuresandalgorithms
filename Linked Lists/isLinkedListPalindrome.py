def isPalindrome(linkedList):
    if(linkedList.head == None or linkedList.head.next == None):
            return True
    arr = []
    curr = linkedList.head
    while curr != None:
        arr.append(curr.data)
        curr = curr.next

    for i in range(len(arr)):
        # check if head and tail are different, if they are then it's not a palindrome
        if(arr[i] != arr[len(arr) - i - 1]):
            return False

    return True
