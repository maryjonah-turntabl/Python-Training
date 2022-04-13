import sys
from testplan import test_plan
from testplan.testing.multitest import MultiTest, testcase, testsuite
import mary_calculator

@testsuite
class CalculatorSuite(object):

    # Happy Case - Add
    @testcase 
    def mary_add(self, env, result):
        result.equal(mary_calculator.addNumbers(2, 4), 6)



    # Happy Case - Subtract
    @testcase 
    def mary_subtract(self, env, result):
        result.equal(mary_calculator.subtractNumbers(20, 8), 12)



    # Happy Case - Multiply
    @testcase 
    def mary_multiply(self, env, result):
        result.equal(mary_calculator.multiplyNumbers(2.5, 1.2), 3.0)



    # Happy Case - Division
    @testcase 
    def mary_divide(self, env, result):
        result.equal(mary_calculator.divideNumbers(60, 15), 4.0)

    # Exception Case - Division
    @testcase 
    def mary_divide_with_zero_divisor(self, env, result):
        with result.raises(ZeroDivisionError):
            mary_calculator.divideNumbers(2, 0)



    
    # Happy Case - Modulo
    @testcase 
    def mary_modulo(self, env, result):
        result.equal(mary_calculator.moduloNumbers(10, 3), 1)

    # Exception Case - Modulo
    @testcase 
    def mary_modulo_with_zero_denominator(self, env, result):
        with result.raises(ZeroDivisionError):
            mary_calculator.moduloNumbers(10, 0)



    # Happy Case - Math Exponent
    @testcase 
    def mary_math_exponent(self, env, result):
        result.equal(mary_calculator.exponentNumbers(0), 1.0)

    
    # Happy Case - Natural Log
    @testcase 
    def mary_natural_log(self, env, result):
        result.equal(mary_calculator.naturalLogNumbers(2), 0.6931471805599453)

    # Exception Case - Natual Log with 0 Base
    @testcase
    def mary_natural_log_with_base_of_zero(self, env, result):
        with result.raises(ValueError):
            mary_calculator.naturalLogNumbers(0)
    
    # Exception Case - Natual Log with Negative Base
    @testcase 
    def mary_natural_log_with_base_negative(self, env, result):
        with result.raises(ValueError):
            mary_calculator.naturalLogNumbers(-5)
            

@test_plan(name='Calculate')
def main(plan):
    test = MultiTest(name='CalculatorTest', suites=[CalculatorSuite()])
    plan.add(test)
    

if __name__ == '__main__':
    sys.exit(not main())        