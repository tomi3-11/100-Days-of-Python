
def main():
    import random
    random.seed(42)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
         random.shuffle(testData)
         assert mode(testData) == 4


def mode(numbers):
# Special case: If the numbers list is empty, return None:
    if len(numbers) == 0:
        return None

    # Dictionary with keys of numbers and values of how often they appear:
    numberCount = {}

# Track the most frequent number and how often it appears:
    mostFreqNumber = None
    mostFreqNumberCount = 0
    
    # Loop through all the numbers, counting how often they appear:
    for number in numbers:
        # If the number hasn't appeared before, set it's count to 0.
        if number not in numberCount:
            numberCount[number] = 0
        # Increment the number's count:
        numberCount[number] += 1

        # If this is more frequent than the most frequent number, it
        # becomes the new most frequent number:
        if numberCount[number] > mostFreqNumberCount:
            mostFreqNumber = number
            mostFreqNumberCount = numberCount[number]

    # The function returns the most frequent number:
    return mostFreqNumber


if __name__ == "__main__":
    main()
