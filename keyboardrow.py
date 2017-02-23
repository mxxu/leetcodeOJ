class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        m = {}
        for i, comb in enumerate(['0123456789', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']):
            for c in comb:
                m[c] = i
                
        buf = []
        for word in words:
            row = -1
            ok = True
            for c in word:
                c = c.lower()
                if c not in m:
                    ok = False
                    break
                if row >= 0 and m[c] != row:
                    ok = False
                    break
                row = m[c]
            if ok:
                buf.append(word)
        return buf
                
s = Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])