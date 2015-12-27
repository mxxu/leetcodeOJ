class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        d = {}
        for s in strs:
            hashed = ''.join(sorted(s))
            d.setdefault(hashed, [])
            d[hashed].append(s)

        ret = []
        for hashed, gps in d.iteritems():
            ret.append(sorted(gps))

        return ret

s = Solution()
r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print r
