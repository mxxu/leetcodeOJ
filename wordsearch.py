class Solution(object):

    def do_exist(self, i, j, board, word, flag, m, n):
        if not word:
            return True

        if i - 1 >= 0 and board[i-1][j] == word[0] and flag[i-1][j] == 0:
            flag[i-1][j] = 1
            if self.do_exist(i-1, j, board, word[1:], flag, m, n):
                return True
            flag[i-1][j] = 0

        if i + 1 < m and board[i+1][j] == word[0] and flag[i+1][j] == 0:
            flag[i+1][j] = 1
            if self.do_exist(i+1, j, board, word[1:], flag, m, n):
                return True
            flag[i+1][j] = 0

        if j - 1 >= 0 and board[i][j-1] == word[0] and flag[i][j-1] == 0:
            flag[i][j-1] = 1
            if self.do_exist(i, j-1, board, word[1:], flag, m, n):
                return True
            flag[i][j-1] = 0

        if j + 1 < n and board[i][j+1] == word[0] and flag[i][j+1] == 0:
            flag[i][j+1] = 1
            if self.do_exist(i, j+1, board, word[1:], flag, m, n):
                return True
            flag[i][j+1] = 0

        return False


    def exist(self, board, word):

        """

        :type board: List[List[str]]

        :type word: str

        :rtype: bool

        """
        if not board or not word:
            return False

        m, n = len(board), len(board[0])
        flag = []
        for i in range(m):
            flag.append([])
            for j in range(n):
                flag[i].append(0)

        for i in range(m):
            row = board[i]
            for j in range(n):
                e = row[j]
                if e == word[0] and flag[i][j] == 0:
                    flag[i][j] = 1
                    if self.do_exist(i, j, board, word[1:], flag, m, n):
                        return True
                    flag[i][j] = 0

        return False

s = Solution()
board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
word = 'ABCCED'
print s.exist(board, word)
word = 'SEE'
print s.exist(board, word)
word = 'ABCB'
print s.exist(board, word)
