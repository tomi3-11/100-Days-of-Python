
def main():
    assert average([1, 2, 3]) == 2
    assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert average([12, 20, 37]) == 23
    assert average([0, 0, 0, 0, 0]) == 0

def average(numbers: list[int]) -> int:
    """Calculates the avarage of numbers in a list."""
    if len(numbers) == 0:
        return 0

    """
    1. initialize sum to zero
    2. loop through the numbers
    3. add each number in the list to the sum
    4. initialize a variable called average
    5. perform the operation (sum / length of numbers)
    6. return average
    """
    total_sum = 0
    for num in numbers:
        total_sum += num

    average = total_sum / len(numbers)

    return average


if __name__ == "__main__":
    main()
