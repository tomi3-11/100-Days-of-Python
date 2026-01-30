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
   
    assert area(10, 10) == 100
    assert area(0, 9999) == 0


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
