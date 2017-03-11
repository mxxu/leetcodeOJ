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
    
    # result = set()
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.solveNQueensByRow(n, [], 0, [], [])
        # self.result.extend([n-i-1 for l in self.result for i in l if l[0] < n/2])
        # return [[self.tostr(n, i)] for q in self.result for i in q]
        return self.result
    
    def tostr(self, n, i):
        l = ['.'] * n
        l[i] = 'Q'
        return ''.join(l)
        
    def solveNQueensByRow(self, n, queens, row, diffset, sumset):
        if row >= n:
            self.result.append([self.tostr(n, i) for i in queens])
            # print queens
            # self.result.append(queens)
            return
            
        # for j in range((n+1)/2):
        for j in range(n):
            # print j
            # if count[row][j] > 0:
                # continue
                
            # self.mark(n, row, j, count, 1)
            
            # s = self.tostr(n, j)
            if j not in queens and row-j not in diffset and row+j not in sumset:
                # queens.append(j)
                self.solveNQueensByRow(n, queens+[j], row+1, diffset+[row-j], sumset+[row+j])
            
            # if row + 1 == n:
#                 buf.append([s])
#                 # print buf, row
#             else:
#                 subret = self.solveNQueensByRow(n, count, row+1)
#                 if subret:
#                     # print subret, row, 'subret', buf, s
#                     for l in subret:
#                         buf.append([s] + l)
                    # print buf, row
                    
            # self.mark(n, row, j, count, -1)
        # return buf
                
if __name__ == '__main__':
    # n = 5
    # count = [[0] * n for _ in range(n)]
    s = Solution()
    print s.solveNQueens(4)
    # s.mark(n, 1, 1, count, 1)
#     print count
#     s.mark(n, 1, 1, count, -1)
#     print count
