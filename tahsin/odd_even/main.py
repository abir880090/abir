

from msilib.schema import Error


def isEven(num):
    """
    Checking if the given is valid.
    """

    if not isinstance(num, int):
        raise ValueError(f"Expected integer as input, but got {type(num)}")

    if num % 2 == 0:
        """
        Checking if the value is even
        """
        return True
    elif num % 2 != 0:
        """
        Checking if the value is odd
        """
        return False


def isEvenList(nums):

    if not isinstance(nums, int):
        """
        Checking if the given value is valid.
        """

        raise ValueError(f"Expected List<int> as input")

    odds = []
    evens = []

    for i in nums:
        """
        Using a for loop for checking each value from the list...
        if it is even or odd.
        """

        if isEven(i) == True:
            evens.append(i)
        elif isEven(i) == False:
            odds.append(i)

    return [evens, odds]


nums = [1]

# print(isEvenList(nums))
print(type(nums))
