class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmaxpre = nums[0]
        ret = nums[0]
        for n in nums[1:]:
            currmax = max(currmaxpre + n, n)
            ret = max(currmax, ret)
            currmaxpre = max(0, currmax)
        return ret
        # return self.divideconquer(nums, 0, len(nums) - 1)
#
#     def divideconquer(self, nums, left, right):
#         if left > right:
#             return 0
#
#         if left == right:
#             return nums[left]
#
#         mid = left + (right - left) / 2
#         l = self.divideconquer(nums, left, mid)
#         r = self.divideconquer(nums, mid+1, right)
#
#         return l if l[1][0] > r[1][0] else r
            
s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
print s.maxSubArray(a)
            
        