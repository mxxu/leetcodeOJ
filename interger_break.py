class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        remainder = n%3
        k = n/3
        
        if remainder == 1:
            k = k - 1
            remainder = 4
        
        ret = 0
        if k > 0:
            ret += 3 ** k
        if ret > 0:
            if remainder > 0:
                return ret * remainder
            else:
                return ret
        return remainder
        
s = Solution()
print s.integerBreak(6)