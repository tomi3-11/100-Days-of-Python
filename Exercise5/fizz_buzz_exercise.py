"""
Here we are writing a function that prints fizzbuzz if a number is divisible by both 3 and 5, prints fizz when divisible by 3, prints buzz if divisible by 5 and prints the number is neither divisible by 3 and 5.

fizzbuzz() -> Handles the fizzbuzz prints
    params:
        upto -> Gives the number to be printed from 1 to it.
"""

def main():
    choice = int(input("Enter the range for the fizzbuzz: "))
    soln = fizzBuzz(choice)
    print(soln)


def fizzBuzz(upTo):
    for i in range(1, upTo):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == "__main__":
    main()
