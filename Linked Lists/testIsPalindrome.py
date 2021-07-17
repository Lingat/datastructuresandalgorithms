import pytest
from singleLinkedList import *
from isLinkedListPalindrome import *

def testSingleCase():
    sll = linkedList(10)
    assert isPalindrome(sll) == True


def testTwoCaseTrue():
    sll = linkedList(10)
    sll.appendToTail(10)
    assert isPalindrome(sll) == True

def testTwoCaseFalse():
    sll = linkedList(10)
    sll.appendToTail(11)
    assert isPalindrome(sll) == False

def testSeveralCaseFalse():
    sll = linkedList(1)
    sll.appendToTail(1)
    sll.appendToTail(0)
    sll.appendToTail(0)
    assert isPalindrome(sll) == False

def testSeveralCaseTrue():
    sll = linkedList(123)
    sll.appendToTail(5)
    sll.appendToTail(5)
    sll.appendToTail(123)
    assert isPalindrome(sll) == True

