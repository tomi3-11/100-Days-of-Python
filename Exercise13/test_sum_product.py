import random, get_sum_and_product, sys

sys.set_int_max_str_digits(0)

numbers = []
for i in range(10000):
    numbers.append(random.randint(1, 1000000000))
print('Numbers:', numbers)
print(' Sum is', get_sum_and_product.calculateSum(numbers))
print('Product is', get_sum_and_product.calculateProduct(numbers))
