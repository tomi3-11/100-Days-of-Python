"""
This program calculates the area and the volume

Functions:
    area() -> Calculates the area
        params:
            length, width
    perimeter() -> Calculates the perimeter 
        params:
            length, width

    Volume() -> Calculates the volume
        params:
            length, width, height

    surfaceArea() -> Calculates the surface area
        params:
            length, width, height
"""

def main():
    

    # Tests for all the functions called.
    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40
    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26
    assert volume(10, 10, 10) ==1000
    assert volume(9999, 0, 9999) == 0
    assert volume(8, 4, 10) == 320
    assert surface_area(10, 10, 10) == 600
    assert surface_area(9999, 0, 9999) ==  199960002 
    assert surface_area(5, 8, 10) == 340


def area(length: int, width: int):
    result = length * width
    return result


def perimeter(length: int, width: int):
    result = 2 * (length + width)
    return result


def volume(length, width, height):
    result = length * width * height
    return result


def surface_area(length, width, height):
    res1 = length * width
    res2 = length * height
    res3 = width * height

    result = (res1 * 2) + (res2 * 2) + (res3 * 2)
    return result


if __name__ == "__main__":
    main()
