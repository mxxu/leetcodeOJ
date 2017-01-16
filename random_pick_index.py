import random

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        n = 0
        ret = -1
        for idx, i in enumerate(self.nums):
            if target != i:
                continue
                
            n += 1
            r = random.random()
            if r < 1.0 / n:
                ret = idx
                
        return ret


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 2, 3, 3, 3])
for i in range(10):
    param_1 = obj.pick(3)
    print param_1