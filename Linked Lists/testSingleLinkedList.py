import pytest
from singleLinkedList import *

'''
@pytest.fixture
def exampleList():
    sll = linkedList(10)
    sll.appendToTail(15)
    sll.appendToTail(20)
    sll.appendToTail(30)
    return list1
'''

def testSllInit():
    sll = linkedList(10)
    assert sll.head.data == 10

def testAppendToTail():
    sll = linkedList(10)
    sll.appendToTail(20)
    sll.appendToTail(30)
    assert sll.head.next.data == 20
    assert sll.head.next.next.data == 30

def testDeleteNode():
    sll = linkedList(10)
    sll.appendToTail(20)
    sll.appendToTail(30)
    sll.deleteNode(20)
    assert sll.head.next.data == 30

def testDeleteHead():
    sll = linkedList(10)
    sll.appendToTail(20)
    sll.appendToTail(30)
    sll.head = sll.deleteNode(10)
    assert sll.head.data == 20

