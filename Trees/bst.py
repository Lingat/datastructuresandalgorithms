class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, data):
        if(data > self.data and node.right == None):
            node.right = TreeNode(data)
        elif(data > self.data and node.right != None):
            node.right.add(data)
        if(data < self.data and node.left == None):
            node.right = TreeNode(data)
        elif(data < self.data and node.left != None):
            node.right.add(data)


            

    
def inOrderTransversal(node): 
    if(node != null):
        inOrderTransversal(node.left)
        print(node)
        inOrderTransversal(node.right)
        