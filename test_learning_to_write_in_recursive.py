import learning_to_write_in_recursive as recursive

def test_ch11_exercise1():
    assert recursive.ch11_exercise1(["ab", "c", "def", "ghij"]) == 10

def test_ch11_exercise2():
    assert recursive.ch11_exercise2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]
    assert recursive.ch11_exercise2([4, 8, 15, 20, 50, 73, 88, 99]) == [4, 8, 20, 50, 88]

def test_ch11_exercise3():
    assert recursive.ch11_exercise3(7) == 28
    assert recursive.ch11_exercise3(8) == 36
    assert recursive.ch11_exercise3(9) == 45
    assert recursive.ch11_exercise3(10) == 55

def test_ch11_exercise4():
    assert recursive.ch11_exercise4("abcdefghijklmnopqrstuvwxyz") == 23