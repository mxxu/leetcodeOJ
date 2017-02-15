class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        maxi, mini = nums[0], nums[0]
        currmax, currmin = None, None
        
        for n in nums[1:]:
            currmax = max(max(maxi * n, mini * n), n)
            currmin = min(min(maxi * n, mini * n), n)
            
            ret = max(ret, currmax)
            
            maxi, mini = currmax, currmin
                
        return ret
        
s = Solution()
print s.maxProduct([2,3,-2,4])
print s.maxProduct([-2])
print s.maxProduct([-2, 0])
print s.maxProduct([0])
print s.maxProduct([-2, -1])
print s.maxProduct([0, 2])
print s.maxProduct([3, -1, 4])
print s.maxProduct([2, -5, -2, -4, 3])