class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        char_idx = {}
        max_len, prev = 0, 0
        for i, c in enumerate(s):
            if c in char_idx:
                prev = max(prev, char_idx[c]+1)

            char_idx[c] = i

            if i - prev + 1 > max_len:
                max_len = i - prev + 1

        return max_len

s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')
print s.lengthOfLongestSubstring('abcad')
print s.lengthOfLongestSubstring('abba')
