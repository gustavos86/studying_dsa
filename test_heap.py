from heap import *

def test_insert1():
    """
    Test inserting a single element
    """
    heap1 = Heap()
    heap1.data_list = [100, 89, 75, 61, 43, 24, 27, 32, 21, 17, 9, 2]
    heap1.insert(55)
    assert heap1.data_list == [100, 89, 75, 61, 43, 55, 27, 32, 21, 17, 9, 2, 24]

def test_insert2():
    """
    Test inserting a single element
    """
    heap1 = Heap()
    heap1.data_list = [10, 9, 8, 6, 5, 7, 4, 2, 1, 3]
    heap1.insert(11)
    assert heap1.data_list == [11, 10, 8, 6, 9, 7, 4, 2, 1, 3, 5]

def test_insert3():
    """
    Test inserting a single element
    """
    heap1 = Heap()
    heap1.data_list = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]
    heap1.insert(40)
    assert heap1.data_list == [100, 88, 40, 87, 16, 25, 12, 86, 50, 2, 15, 3, 8]

def test_delete1():
    """
    Test deleting a single element
    """
    heap1 = Heap()
    heap1.data_list = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]
    heap1.delete()
    assert heap1.data_list == [88, 87, 25, 86, 16, 8, 12, 3, 50, 2, 15]