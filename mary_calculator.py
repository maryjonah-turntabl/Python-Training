import math

def addNumbers(num1, num2):
    return num1 + num2

def subtractNumbers(num1, num2):
    return num1 - num2

def multiplyNumbers(num1, num2):
    return num1 * num2;

def divideNumbers(numerator, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return numerator / divisor

def moduloNumbers(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot find the remainder of 0")
    return num1 % num2    

def exponentNumbers(exponent):
    return math.exp(exponent)

def naturalLogNumbers(base):
    if base <= 0:
        raise ValueError("Base cannot be 0 or lower than 0")
    return math.log(base)