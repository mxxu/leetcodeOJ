class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, y, z = nums[0], None, None
        
        for n in nums[1:]:
            if n == x or n == y or n == z:
                continue
                
            if n > x:
                x, y, z = n, x, y
            elif n > y or y is None:
                y, z = n, y
            elif n > z or z is None:
                z = n
        return z if z != None else x
        
s = Solution()
for l in ([3, 2, 1], [1, 2], [2,2,3,1]):
    print s.thirdMax(l)