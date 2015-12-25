class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        i = 0
        begin = 0
        n = len(nums)
        ret = []

        while i < n:
            while i+1 < n and nums[i+1] == nums[i] + 1:
                i += 1

            if i == begin:
                ret.append("%s" % nums[i])
            else:
                ret.append("%s->%s" % (nums[begin], nums[i]))
            i += 1
            begin = i

        return ret

s = Solution()
x = s.summaryRanges([0, 1, 2, 4,5,7])
print x

