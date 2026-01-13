def main():
    num = int(input("Enter number: "))
    result = is_even(num)
    print(result)

    res = is_odd(num)
    print(res)

    # Tests
    assert is_even(4)
    assert is_odd(7)


def is_even(num):
    result = False
    if num % 2 == 0:
        result = True

    return result


def is_odd(num):
    result = False
    if num % 2 != 0:
        result = True

    return result


if __name__ == "__main__":
    main()
