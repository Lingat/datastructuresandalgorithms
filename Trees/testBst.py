import pytest
from bst import *

def testSearch():
    node = TreeNode(50)
    node.add(2)
    node.add(-1)
    node.add(10)
    node.add(5)
    node.add(20)
    node.add(2)
    node.add(60)
    node.add(55)
    node.add(65)
    assert inBST(node, 20) == True
    assert inBST(node, 60) == True
    assert inBST(node, 50) == True
    assert inBST(node, 115) == False
    assert inBST(node, -2) == False
    assert inBST(node, 0) == False
    