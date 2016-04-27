class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_chars = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        f = lambda c: c in vowel_chars
        vowels = [c for c in s if f(c)][::-1]
        buf = []
        i = 0
        for c in s:
            if f(c):
                buf.append(vowels[i])
                i += 1
            else:
                buf.append(c)
                
        return ''.join(buf)
        
s = Solution()
print s.reverseVowels('aA')