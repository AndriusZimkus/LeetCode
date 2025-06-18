class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = 0
        isNegative = 1
        if x < 0:
            isNegative = -1
            x = abs(x)
            
        while x >= 1:
            current = x % 10
            result = result*10 + current
            x //= 10
            
        result = result * isNegative

        maxValue = 2**31-1
        minValue = -2**31
        if result > maxValue or result < minValue:
            result = 0
        return result
