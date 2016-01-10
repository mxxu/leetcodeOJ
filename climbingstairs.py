class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 2:
            return n
        
        buf = [1, 1]
        for i in range(2, n+1):
            buf.append(buf[i-1] + buf[i-2])
        return buf[-1]
        
s = Solution()
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(3)
print s.climbStairs(4)
print s.climbStairs(5)