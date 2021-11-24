class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, data):
        if(data > self.data and self.right == None):
            self.right = TreeNode(data)
        elif(data > self.data and self.right != None):
            self.right.add(data)
        if(data < self.data and self.left == None):
            self.left = TreeNode(data)
        elif(data < self.data and self.left != None):
            self.left.add(data)
    
  



def findMax(a, b):
    if a >= b:
      return a;
    else:
      return b;

def height(root):
    # Base case:
    if root is None:
        return 0;

    return findMax(height(root.left), height(root.right)) + 1;


def inBST(node, data):
    if node == None:
        return False
    elif data == node.data:
        return True
    elif data > node.data:
        return inBST(node.right, data)
    elif data < node.data:
        return inBST(node.left, data)

            

    
def inOrderTransversal(node): 
    if(node != None):
        inOrderTransversal(node.left)
        print(node.data)
        inOrderTransversal(node.right)

def printLevelOrder(node):
    h = height(node)
    spacing = h
    for i in range(1, h + 1):
        print(" " * spacing, end="")
        printGivenLevel(node, i)
        print()
        spacing-=i

def printGivenLevel(node, level):
    if node is None:
        print("", end = ' ')
        return node
     
    if level == 1:
        print(node.data, end = ' ')
    elif level > 1:
        printGivenLevel(node.left, level - 1)
        printGivenLevel(node.right, level - 1)
        





# inOrderTransversal(node)

printLevelOrder(node)

print(inBST(node, 21230))