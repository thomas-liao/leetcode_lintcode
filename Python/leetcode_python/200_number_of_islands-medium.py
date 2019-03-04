# solution 1, bfs
# from collections import deque
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         counter = 0
#         m, n = len(grid), len(grid[0])
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     counter += 1
#                     self.wipeIsland(grid, i, j)
#         return counter
        
#     def wipeIsland(self, grid, i, j):
#         if not grid or not grid[0]:
#             return
#         assert grid[i][j] == '1'
#         grid[i][j] = '0'
#         q = deque()
#         q.append((i, j))
#         m, n = len(grid), len(grid[0])
        
#         while q:
#             x, y = q.popleft()            
#             for x_nei, y_nei in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
#                 if x_nei >=  0 and x_nei < m and y_nei >= 0 and y_nei < n and grid[x_nei][y_nei] == '1':
#                     grid[x_nei][y_nei] = '0'
#                     q.append((x_nei, y_nei))




# solution 2, dfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    counter += 1
                    self.sinkIsland(grid, i, j)
        return counter
        
    def sinkIsland(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
            grid[i][j] = '0'            
            
            # equivalent to
            self.sinkIsland(grid, i - 1, j)
            self.sinkIsland(grid, i+1, j)
            self.sinkIsland(grid, i, j - 1)
            self.sinkIsland(grid, i, j + 1)
            
            
            #  map(self.sinkIsland, (i-1, i+1, i, i), (j, j, j-1, j+1)) doesn't work, whyyyy?
