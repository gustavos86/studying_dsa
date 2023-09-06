from quicksort import QuickSort

def test_partition1():
    qs = QuickSort([0, 5, 2, 1, 6, 3])

    result = qs._partition(0, len(qs.array)-1)
    
    assert result == 3

def test_quicksort1():
    qs = QuickSort([0, 5, 2, 1, 6, 3])

    qs.quicksort()
    
    assert qs.array == [0, 1, 2, 3, 5, 6]


def test_quicksort2():
    qs = QuickSort([2, 6, 4, 5, 3, 1, 9, 8, 7, 0])

    qs.quicksort()
    
    assert qs.array == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]