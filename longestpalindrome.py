class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        for c in s:
            h[c] = h.get(c, 0) + 1
        hasodd = False
        ret = 0
        for k in h.itervalues():
            if k % 2 == 0:
                ret += k
            else:
                hasodd = True
                ret += k - 1
        if hasodd:
            ret += 1
        return ret
s = Solution()
print s.longestPalindrome('abccccdd')