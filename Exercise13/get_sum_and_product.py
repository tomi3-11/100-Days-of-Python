def main():
    assert calculateSum([]) == 0
    assert calculateSum([2, 4, 6, 8, 10]) == 30
    assert calculateProduct([]) == 1
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840
            

def calculateSum(numbers: list[int])-> int:
    """This calculates the sum and returns the total sum of the list."""
    # Return zero if the list is empty
    if len(numbers) == 0:
        return 0
    
    """
    1. set sum to zero
    2. loop through all the numbers in the list
    3. add each to the sum
    4. return the sum
    """
    total_sum = 0
    for num in numbers:
        total_sum += num

    return total_sum


def calculateProduct(numbers: list[int])-> int:
    """This calculates the product and returns the product of the list."""
    # Return zero if the list is empty
    if len(numbers) == 0:
        return 1
    
    """
    1. set product to zero
    2. loop through all the numbers in the list
    3. multiply each number with the product
    4. return the product
    """
    product = 1
    for num in numbers:
        product *= num

    return product


if __name__ == "__main__":
    main()
