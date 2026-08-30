class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for 32-bit signed integer overflow before adding next digit
            # 2^31 - 1 = 2147483647
            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and digit > 7):
                return 0
                
            reversed_x = reversed_x * 10 + digit
            
        return sign * reversed_x