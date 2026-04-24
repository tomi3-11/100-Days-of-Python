
def main():
    assert mode([]) == None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1

def mode(numbers: list[int]):
    """Calculates the mode from the list of numbers."""
    if len(numbers) == 0:
        return None

    freq = {}

    for num in numbers:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    mode = 0
    for key in freq:
       if freq[key] > mode:
           mode = key
    return mode


if __name__ == "__main__":
    main()
