import pytest
import random
from mergeSort import *

def testSingle():
    arr = [0]
    mergeSort(arr)
    assert arr == [0]
def testSorted():
    arr = [1, 2, 3, 4]
    mergeSort(arr)
    assert arr == [1, 2, 3, 4]

def testDescending():
    arr = [4, 3, 2, 1]
    mergeSort(arr)
    assert arr == [1, 2, 3, 4]

def testRandom():
    arr = [1, -1235, 2, 3, 18, 19, 20, 21, 22, 25, 28, 29, 30, 50, 100, 200, 300, 400, 500, 600, 820, 925, 1000, 1200, 1205, 1206, 1999, 2500, 2501, 2699, 8300]
    random.shuffle(arr)
    mergeSort(arr)
    assert arr == [-1235, 1, 2, 3, 18, 19, 20, 21, 22, 25, 28, 29, 30, 50, 100, 200, 300, 400, 500, 600, 820, 925, 1000, 1200, 1205, 1206, 1999, 2500, 2501, 2699, 8300]

