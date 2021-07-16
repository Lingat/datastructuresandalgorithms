class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, data):
        self.head = Node(data)

    def printList(self):
        curr = self.head
        while curr != None:
            if curr.next != None:
                print(curr.data, end = ' -> ')
            else:
                print(curr.data)
            curr = curr.next
    
    def deleteNode(self, data):
        prev = self.head
        curr = self.head
        if(data == self.head.data):
            print(self.head.next.data)
            return self.head.next
        
        
        while curr != None:
            if curr.data == data:
                prev.next = curr.next
                return self.head
            prev = curr
            curr = curr.next
    
    def appendToTail(self, end):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(end)

list1 = linkedList(10)
list1.appendToTail(15)
list1.head = list1.deleteNode(15)
list1.printList()


