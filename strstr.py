class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1

        i, j = 0, 0
        m, n = len(haystack), len(needle)

        while i <= m - n:
            j = 0
            k = i
            while j < n and needle[j] == haystack[k]:
                k += 1
                j += 1

            if j == n:
                return i

            i += 1
        return -1

s = Solution()
print s.strStr('12312412asfasfd', 'fas')
