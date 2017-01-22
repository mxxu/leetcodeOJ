class Solution(object):
    def mark(self, n, i, j, count, k=1):
        for idx in range(n):
            count[i][idx] += k
            count[idx][j] += k
        count[i][j] -= k
        r, c = i - 1, j - 1
        while r >= 0 and c >= 0:
            count[r][c] += k
            r -= 1
            c -= 1
        r, c = i - 1, j + 1
        while r >= 0 and c < n:
            count[r][c] += k
            r -= 1
            c += 1
        r, c = i + 1, j - 1
        while r < n and c >= 0:
            count[r][c] += k
            r += 1
            c -= 1
        r, c = i + 1, j + 1
        while r < n and c < n:
            count[r][c] += k
            r += 1
            c += 1
    
    result = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # count = [[0] * n for _ in range(n)]
        return self.solveNQueensByRow(n, [], 0)
    
    def tostr(self, n, i):
        l = ['.'] * n
        l[i] = 'Q'
        return ''.join(l)
        
    def solveNQueensByRow(self, n, queens, row):
        if row >= n:
            return buf
            
        for j in range(n):
            if count[row][j] > 0:
                continue
                
            self.mark(n, row, j, count, 1)
            
            s = self.tostr(n, j)
            
            if row + 1 == n:
                buf.append([s])
                # print buf, row
            else:
                subret = self.solveNQueensByRow(n, count, row+1)
                if subret:
                    # print subret, row, 'subret', buf, s
                    for l in subret:
                        buf.append([s] + l)
                    # print buf, row
                    
            self.mark(n, row, j, count, -1)
        return buf
                
if __name__ == '__main__':
    n = 5
    count = [[0] * n for _ in range(n)]
    s = Solution()
    print s.solveNQueens(5)
    # s.mark(n, 1, 1, count, 1)
#     print count
#     s.mark(n, 1, 1, count, -1)
#     print count
