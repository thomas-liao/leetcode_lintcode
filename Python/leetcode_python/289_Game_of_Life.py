class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        new_board = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_board[i][j] = self.checkState(board, (i, j))
        # for i in range(m):
        #     for j in range(n):
        #         board[i][j] = new_board[i][j]
        # or you could do it this way
        board[:] = new_board[:]
    
    def checkState(self, board, p):
        neis = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        x = p[0]
        y = p[1]
        m = len(board)
        n = len(board[0])
        live_count = 0
        for nei in neis:
            nei_p = (x + nei[0], y + nei[1])
            xx = nei_p[0]
            yy = nei_p[1]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if board[xx][yy] == 1:
                live_count += 1
        
        if board[x][y] == 0:
            # reproduction
            if live_count == 3:
                return 1
            else:
                return 0
        if board[x][y] == 1:
            # under population
            if live_count < 2:
                return 0
            # next generation
            elif live_count == 2 or live_count == 3:
                return 1
            else:
                # over population
                return 0
        raise Exception("Shouldn't reach here")
        
