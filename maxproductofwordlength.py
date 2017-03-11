class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words or len(words) <= 1:
            return 0
        n = len(words)

        def binstr(s):
            n = 0
            for c in s:
                n = n | (1 << (ord(c) - 97))
            return n
        bins = [binstr(w) for w in words]
            
        ret = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if bins[i] & bins[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret
        
s = Solution()
print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
print s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
print s.maxProduct(["a", "aa", "aaa", "aaaa"])