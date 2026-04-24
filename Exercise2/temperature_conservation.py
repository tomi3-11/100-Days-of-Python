"""
Exercise 2: Temperature Conversion.

Use these two formulas for converting between Celsius and Fahrenheit: 
- Fahrenheit = Celsius × (9 / 5) + 32 
- Celsius = (Fahrenheit - 32) × (5 / 9)

Steps:
- Write a convertToFahrenheit() function.
    - with a degreesCelsius parameter
    - function returns the temperature in degrees Fahrenheit. 
- Write a convertToCelsius() function. 
    - with a degreesFahrenheit parameter
    - Function returns the temperature in degrees Celsius. 

"""

# Code for the solution

def convertToFahrenheit(degreescelsius):
    result = degreescelsius * (9/5) + 32
    return result



def convertToCelsius(degreesFahrenheit):
    result = (degreesFahrenheit - 32) * (5/9)
    return result
    
    
def main():
    print(convertToCelsius(230))
    print(convertToFahrenheit(12))
    
    
if __name__ == "__main__":
    main()
    
    
    
# Tests

assert convertToCelsius(0) == -17.77777777777778 
assert convertToCelsius(180) == 82.22222222222223 
assert convertToFahrenheit(0) == 32 
assert convertToFahrenheit(100) == 212 
assert convertToCelsius(convertToFahrenheit(15)) == 15 

# Rounding errors cause a slight discrepancy: 
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001


"""
Solution Template

def convertToFahrenheit(degreesCelsius): 
# Calculate and return the degrees Fahrenheit: 
    return ____ * (9 / 5) + 32 
    
def convertToCelsius(degreesFahrenheit): 
# Calculate and return the degrees Celsius: 
    return (____ - 32) * (____ / ____) 


"""

