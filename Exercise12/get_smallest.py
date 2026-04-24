def main():
#    numbers = [4, 2, 54, 23, 87]
#    ans = getSmallest(numbers)
#    print(ans)

    assert getSmallest([1, 2, 3]) == 1
    assert getSmallest([3, 2, 1]) == 1
    assert getSmallest([28, 25, 42, 2, 28]) == 2
    assert getSmallest([1]) == 1
    assert getSmallest([]) == None
    

def getSmallest(numbers):
    """Getting the smallest value from a list of numbers."""

    # return none if list is empty
    if len(numbers) == 0:
        return None

    # set the smallest number as the first value in the list
    min_val = numbers[0]

    """
    1. Loop through the whole list
    2. check individual member against the smallest value initialized
    3. set the smallest if found
    4. return the smallest value
    """
    for i in range(len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]

    return min_val


if __name__ == "__main__":
    main()
    
