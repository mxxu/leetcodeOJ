class Solution(object):
    def go(self, s, k, palindrome):
        n = len(s)
        if k >= n:
            return [[]]
        if k == n-1:
            return [[s[k]]]
            
        ret = []
        for i in range(k, n):
            if palindrome[(k, i)]:
                result = self.go(s, i+1, palindrome)
                for buf in result:
                    buf.insert(0, s[k:i+1])
                    ret.append(buf)
        # print k, ret
        return ret
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
            
        n = len(s)
        palindrome = {}
        for i in range(n):
            palindrome[(i, i)] = True
            for j in range(i):
                if j+1 == i:
                    palindrome[(j, i)] = s[j] == s[i]
                else:
                    if palindrome[(j+1, i-1)]:
                        palindrome[(j, i)] = s[j] == s[i]
                    else:
                        palindrome[(j, i)] = False
                        
        # print palindrome
        return self.go(s, 0, palindrome)
        
s = Solution()
print s.partition('aab')