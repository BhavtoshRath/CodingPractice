# https://leetcode.com/problems/fraction-to-recurring-decimal/

def fractionToDecimal( numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    remainder = numerator % denominator
    remainder *= 10
    remainder = remainder % denominator
    return remainder



print(fractionToDecimal( 1, 3))
