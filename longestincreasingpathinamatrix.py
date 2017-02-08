class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        C = []
        for i in range(m):
            C.append([-1] * n)
        # print C
        
        depth = 0
        for i in range(m):
            for j in range(n):
                depth = max(depth, self.depthfirstsearch(matrix, C, i, j, m, n))
        return depth
        
    def neighbours(self, x, y, m, n):
        buf = []
        for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if a >= 0 and b >= 0 and a < m and b < n:
                buf.append((a, b))
        return buf
        
    def depthfirstsearch(self, matrix, C, x, y, m, n):
        if C[x][y] > 0:
            return C[x][y]
        depth = 1
        for a, b in self.neighbours(x, y, m, n):
            if matrix[a][b] > matrix[x][y]:
                depth = max(depth, 1 + self.depthfirstsearch(matrix, C, a, b, m, n))
        C[x][y] = depth
        return depth
        
        
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

nums2 = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

nums2 = [
  [3,3,3],
  [3,3,3],
  [3,3,3]
]

s = Solution()

print s.longestIncreasingPath(nums)
print s.longestIncreasingPath(nums2)