import pytest 
import mary_calculator

def test_add():
    assert mary_calculator.addNumbers(10, 20) == 30

def test_subtract():
    assert mary_calculator.subtractNumbers(20, 8) == 12

def test_multiply():
    assert mary_calculator.multiplyNumbers(2.5, 1.2) == 3.0

def test_divide():
    assert mary_calculator.divideNumbers(60, 15) == 4.0

def test_divide_with_zero_divisor():
        with pytest.raises(ZeroDivisionError):
            mary_calculator.divideNumbers(2, 0)

def test_modulo():
    assert mary_calculator.moduloNumbers(10, 3) == 1

def test_modulo_with_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        mary_calculator.moduloNumbers(10, 0)

def test_math_exponent():
    assert mary_calculator.exponentNumbers(0) == 1.0

def test_natural_log():
    assert mary_calculator.naturalLogNumbers(2) == 0.6931471805599453

def test_natural_log_with_base_of_zero():
    with pytest.raises(ValueError):
        mary_calculator.naturalLogNumbers(0)
    
def test_natural_log_with_base_negative():
    with pytest.raises(ValueError):
        mary_calculator.naturalLogNumbers(-5)
