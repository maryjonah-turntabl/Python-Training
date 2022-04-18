from audioop import mul
import math
from re import sub

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

addNumbers(10, 20)
subtractNumbers(20, 8)
multiplyNumbers(10, 2)
# divideNumbers(2, 0)
moduloNumbers(10, 3)
exponentNumbers(0)
naturalLogNumbers(2)