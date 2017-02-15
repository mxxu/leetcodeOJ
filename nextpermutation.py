class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
            
        n = len(nums)
        j = n - 2
        while j >= 0 and nums[j] >= nums[j+1]:
            j -= 1
            
        if j < 0:
            nums[:] = nums[::-1]
            return
            
        up, down = j+1, j
        j = n - 1
        while j >= 0 and nums[j] <= nums[down]:
            j -= 1
        nums[down], nums[j] = nums[j], nums[down]
        nums[up:] = nums[up:][::-1]
        
s = Solution()
for nums in ([1,2,3], [1,3,2], [3,2,1], [1,1,5]):
    print nums
    s.nextPermutation(nums)
    print nums
    print '-------'