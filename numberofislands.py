class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        seq = 0
        seq_union = {}
        island = {}
        
        # i, j = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                up, left = -1, -1
                if i > 0 and (i-1, j) in island:
                    up = island[(i-1, j)]
                if j > 0 and (i, j-1) in island:
                    left = island[(i, j-1)]
                    
                if up < 0 and left < 0:
                    island[(i, j)] = seq
                    seq_union[seq] = seq
                    seq += 1
                    continue
                    
                if up >= 0 and left >= 0:
                    minseq = min(up, left)
                    island[(i, j)] = minseq
                    seq_union[up] = minseq
                    seq_union[left] = minseq
                    continue
                    
                island[(i, j)] = max(up, left)
            # print seq_union
        for k in seq_union:
            while seq_union[k] != k:
                seq_union[k] = seq_union[seq_union[k]]
                k = seq_union[k]
        # print seq_union
        return len(set(seq_union.values()))
s = Solution()
grid = [
    list('11110'),
    list('11010'),
    list('11000'),
    list('00000'),
]
print s.numIslands(grid)

grid2 = [
    list('11000'),
    list('11000'),
    list('00100'),
    list('00011'),
]
print s.numIslands(grid2)
grid3 = [
    '111',
    '010',
    '111'
]
print s.numIslands(grid3)
grid4 = ["1111111","0000001","1111101","1000101","1010101","1011101","1111111"]
print s.numIslands(grid4)