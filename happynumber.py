class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = set()
        
        while n not in m:
            m.add(n)
            x = n
            s = 0
            while x > 0:
                k = x%10
                s += k*k
                x = (x - k)/10
            
            if s == 1:
                return True
                
            n = s
        return False
            
s = Solution()
for n in (0, 1, 19, 82, 68, 100, 67, 86, 91, 2):
    print s.isHappy(n), n