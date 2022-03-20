import pytest
import checkEven

def testSingle():
    assert checkEven.isEven(1) == False
    assert checkEven.isEven(2) == True
    with pytest.raises(ValueError) as e:
        checkEven.isEven('is this a int?😕')
        
def testMulti():
    res = checkEven.isEvenList([1,2,3,4])
    assert res.get("1") == False
    assert res.get("2") == True
    assert res.get("3") == False
    assert res.get("4") == True
    with pytest.raises(ValueError) as e:
        checkEven.isEvenList('is this a list?😕')