class Solution(object):

    def subsets(self, nums):

        """

        :type nums: List[int]

        :rtype: List[List[int]]

        """

        if not nums:
            return []

        res = self.subsets(nums[1:])
        buf = []
        for x in res:
            buf.append(x)
            buf.append()
        return [
            res,
            [[nums[0]] + x for x in res if x],
        ]

s = Solution()
print s.subsets([1,2,3])

