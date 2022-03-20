from main import isEven, isEvenList


def test1():
    assert isEven(2) == True


def test2():
    assert isEven(9) == False


def test3():
    assert isEven(100) == True


def test4():
    assert isEvenList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[0] == [2, 4, 6, 8, 10]


def test5():
    assert isEvenList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])[1] == [1, 3, 5, 7, 9]
