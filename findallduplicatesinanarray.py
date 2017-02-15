class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        i, n = 0, len(nums)
        while i < n:
            while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                k = nums[i]
                nums[i] = nums[k-1]
                nums[k-1] = k
                
            i += 1
            
        return [n for i, n in enumerate(nums) if n != i+1]
s = Solution()
nums=[4,3,2,7,8,2,3,1]
print s.findDuplicates(nums)