class Solution(object):

    def containsNearbyDuplicate(self, nums, k):

        """

        :type nums: List[int]

        :type k: int

        :rtype: bool

        """

        if not nums or k <= 0:
            return False

        n = len(nums)
        if n < 2:
            return False

        buf = [(i, e) for i, e in enumerate(nums)]
        sortbuf = sorted(buf, key=lambda e: e[1])

        for i in range(n-1):
            curr, next = sortbuf[i], sortbuf[i+1]
            if curr[1] == next[1] and abs(curr[0] - next[0]) <= k:
                return True

        return False

s = Solution()
print s.containsNearbyDuplicate([1, 1, 2, 2, 3], 1)
print s.containsNearbyDuplicate([1, 4, 2, 5, 3], 8)
print s.containsNearbyDuplicate([1, 4, 2, 1, 3], 2)
