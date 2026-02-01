"""
Here we are writing a function that can appends an ordinal sign at the end.

Function:
    ordinalSuffix() -> adds an ordinal sign to the end of a given number

    Parameter:
        number

"""

def main():
    assert ordinalSuffix(0) == '0th'
    assert ordinalSuffix(1) == '1st'
    assert ordinalSuffix(2) == '2nd'
    assert ordinalSuffix(3) == '3rd'
    assert ordinalSuffix(4) == '4th'
    assert ordinalSuffix(10) == '10th'
    assert ordinalSuffix(11) == '11th'
    assert ordinalSuffix(12) == '12th'
    assert ordinalSuffix(13) == '13th'
    assert ordinalSuffix(14) == '14th'
    assert ordinalSuffix(101) == '101st'


def ordinalSuffix(number):
    if number[-1] == 1:
        return f"{number}st"
    elif number[-1] == 2:
        return f"{number}nd"
    elif number[-1] == 3:
        return f"{number}rd"
    elif number[-1] == 0 and 3 < number[-1] < 10:
        return f"{number}nd"



if __name__ == "__main__":
    main()
