class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c, m = 0, 0
        for i in nums:
            if i == 0:
                c = 0
            else:
                c += 1
                if m < c:
                    m = c
                    
        return m
                    
s = Solution()
print s.findMaxConsecutiveOnes([1,1,0,1,1,1])