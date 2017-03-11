class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.H = {}
        self.max = [i for i in nums]
        self.min = [-i for i in nums]
        n = len(nums)
        for i in range(n-2, -1, -1):
            self.max[i] = self.max[i+1] + self.max[i]
            self.min[i] = self.min[i+1] + self.min[i]
        self.DFS(S, nums, 0)
        
        return self.H.get((S, 0), 0)
        
    def DFS(self, target, nums, p):
        if not nums and target == 0:
            return 1
            
        if not nums and target != 0:
            return 0
            
        if (target, p) in self.H:
            return self.H[(target, p)]
            
        if self.max[p] < target or self.min[p] > target:
            return 0
            
        r = self.DFS(target-nums[0], nums[1:], p+1) + self.DFS(target+nums[0], nums[1:], p+1)
        self.H[(target, p)] = r
        return r
        
s = Solution()
print s.findTargetSumWays([1,1,1,1,1], -3)
            
        