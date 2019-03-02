# solution 1, using sets
# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         if not matrix or not matrix[0]:
#             return
#         m, n = len(matrix), len(matrix[0])
#         rows, cols = set(), set()
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)
#         for r in rows:
#             self.wipeRow(matrix, r)
#         for c in cols:
#             self.wipeCol(matrix, c)
        
#     def wipeRow(self, matrix, row):
#         for i in range(len(matrix[0])):
#             matrix[row][i] = 0

#     def wipeCol(self, matrix, col):
#         for i in range(len(matrix)):
#             matrix[i][col] = 0


# solution 2, usg first row/col to mark if it needs to be wipped or not (project 0 onto it)
# but note, we need to first check if this first row, col itself contains 0

class Solution(object):
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False
        
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                row_zero = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # mark by projection
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    
    
        for i in range(1, m):
            if matrix[i][0] == 0:
                self.wipeRow(matrix, i, True)
                
        for i in range(1, n):
            if matrix[0][i] == 0:
                self.wipeCol(matrix, i, True)

     
        if row_zero:
            self.wipeRow(matrix, 0)
        if col_zero:
            self.wipeCol(matrix, 0)
                
            
    def wipeRow(self, matrix, row, plusOne=False):
        if not matrix or not matrix[0]:
            return
        for i in range(plusOne, len(matrix[0])):
            matrix[row][i] = 0
    
    def wipeCol(self, matrix, col, plusOne=False):
        if not matrix or not matrix[0]:
            return
        for i in range(plusOne, len(matrix)):
            matrix[i][col] = 0
        
        
        
