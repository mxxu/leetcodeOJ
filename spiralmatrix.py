class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
            
        m = len(matrix)
        n = len(matrix[0])
        maxi = min((m-1)/2, (n-1)/2)
        
        buf = []
        for i in range(maxi+1):
            print i, maxi, m, n
            # if i == n-i-1:
                # buf.append(matrix[i][i])
                # continue
            for j in range(i, n-i):
                buf.append(matrix[i][j])
            for j in range(i+1, m-i-1):
                buf.append(matrix[j][n-i-1])
            # print buf
            if m-i-1 > i:
                for j in range(n-i-1, i-1, -1):
                    buf.append(matrix[m-i-1][j])
            if n-i-1 > i:
                for j in range(m-i-2, i, -1):
                    buf.append(matrix[j][i])
        return buf
s = Solution()
matrix = [
 [ 1, 2, 3, 10 ],
 [ 4, 5, 6, 11 ],
 [ 7, 8, 9, 12 ]
]
matrix2 = [[7], [9], [6]]
matrix3 = [[2,5,8],[4,0,-1]]
print s.spiralOrder(matrix)