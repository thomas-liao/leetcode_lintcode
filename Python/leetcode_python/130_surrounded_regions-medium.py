# solution 1
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    self.marker(board, i, j)
        print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        
    def marker(self, board, i, j):
        m, n = len(board), len(board[0])
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = '#'
            self.marker(board, i + 1, j)
            self.marker(board, i - 1, j)
            self.marker(board, i, j - 1)
            self.marker(board, i, j + 1)
