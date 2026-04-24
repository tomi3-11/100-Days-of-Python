
def main():
    assert median([]) == None
    assert median([1, 2, 3]) == 2
    assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
    assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

def median(numbers: list[int]) -> int:
    """Calculates the median of numbers in a list."""

    # Sort the list in ascending order, get size and initialize median
    numbers.sort()
    size = len(numbers)
    median = 0

    # return none if list is empty
    if size == 0:
        return None

    """
    Check if even, perform floor division and get the average of the 2 mids
    check if odd, perform floor div and get the middle value
    """
    if size % 2 == 0:
        mid = size // 2
        median = ( numbers[mid] + numbers[mid-1] ) / 2
    else:
        mid = size // 2
        median = numbers[mid]

    return median


if __name__ == "__main__":
    main()
