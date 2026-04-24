import random, get_mode

random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert get_mode.mode(testData) == 4
