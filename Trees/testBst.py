import pytest
from bst import *

def testSingle():
    node = TreeNode(1)
    inOrderTransversal(node)
    