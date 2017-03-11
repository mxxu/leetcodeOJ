class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, n = 0, len(nums)
        while i < n:
            k = nums[i]
            if k == i+1 or k == nums[k-1]:
                i += 1
                continue
            nums[i] = nums[k-1]
            nums[k-1] = k
        return [i+1 for i, n in enumerate(nums) if i+1 != n]
        
s = Solution()
print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])