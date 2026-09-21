class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Convert to absolute values
        a = abs(dividend)
        b = abs(divisor)

        quotient = 0

        # Bitwise subtraction
        while a >= b:
            temp = b
            multiple = 1
            # Double temp until it exceeds remaining dividend
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        # Clamp to 32-bit signed integer range
        return min(max(INT_MIN, quotient), INT_MAX)