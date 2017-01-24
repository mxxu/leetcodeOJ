class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = set()
        self.flag = {}
        self.n = len(nums)
        for i in range(self.n-1):
            for j in range(self.n-1, i, -1):
                if nums[j] >= nums[i]:
                    self.flag[(i, j)] = j
                else:
                    self.flag[(i, j)] = self.n+1 if j == self.n-1 else self.flag[(i, j+1)]

        self.DFS([], nums, 0)
        # print self.flag
        
        return [list(t) for t in self.result]
        
    def DFS(self, seqs, nums, p):
        if p >= self.n:
            if len(seqs) >= 2:
                x = tuple([nums[i] for i in seqs])
                # print seqs, x
                if x not in self.result:
                    self.result.add(x)
            return
            
        nextidx = p if not seqs else self.flag[(seqs[-1], p)]
        # print p, nextidx, seqs
        if nextidx > self.n:
            if len(seqs) >= 2:
                x = tuple([nums[i] for i in seqs])
                # print seqs, x
                if x not in self.result:
                    self.result.add(x)
            return
            
        self.DFS(seqs+[nextidx], nums, self.flag.get((nextidx, nextidx+1), self.n+1))
        self.DFS(seqs, nums, nextidx+1)
        
s = Solution()
print s.findSubsequences([1,2,3,2,1])