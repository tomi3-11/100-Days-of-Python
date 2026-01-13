def main():
    num = int(input("Enter number: "))
    result = is_even(num)
    print(result)

    # Tests
    assert is_even(4)


def is_even(num):
    result = False
    if num % 2 == 0:
        result = True

    return result


def is_odd(int: num):
    ...


if __name__ == "__main__":
    main()
