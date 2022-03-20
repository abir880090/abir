#!/usr/bin/python3

def isEven(num):
    # TODO: comment out the type check if num always going to be a int.
    # it will speed up computation for huge amount of numbers while calling form
    # isEvenList() func.
    if not isinstance(num, int):
        raise ValueError(f'isEven() takes "<int>" as argument recived {type(num)} instead!')
    
    if num%2==0:
        return True
    return False


def isEvenList(numList):
    # TODO: comment out the type check if you dont need it.
    # it wont make a big difference.
    if not isinstance(numList, list):
        raise ValueError(f'isEvenList() takes "<list>" as argument recived {type(numList)} instead!')
    
    # use a for loop in numList.
    # store all the results in a dictionary.
    results = {}
    for i in numList:
        results[str(i)] = isEven(i)
    return results
    