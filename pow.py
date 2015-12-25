class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if x == 0:
            return 0

        if n == 1:
            return x

        if n == 2:
            return x * x

        neg = n < 0
        if neg:
            n = -1 * n

        half = self.myPow(x, n/2)

        if n%2 == 0:
            res = half * half
        else:
            res = half * half * x

        if neg:
            return 1.0 / res
        else:
            return res

s = Solution()
print s.myPow(2, 4)
print s.myPow(2, 7)
print s.myPow(2, -7)
