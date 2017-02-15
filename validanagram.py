class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
            
        if not s or not t:
            return False
            
        m, n = len(s), len(t)
        if m != n:
            return False
            
        cs, ct = {}, {}
        for c in s:
            cs[c] = cs.get(c, 0) + 1
            
        for c in t:
            if c not in cs:
                return False
            ct[c] = ct.get(c, 0) + 1
        for c in ct:
            if ct[c] != cs[c]:
                return False
        return True
        
s = Solution()
print s.isAnagram('anagram', 'nagaram')
print s.isAnagram('rat', 'car')