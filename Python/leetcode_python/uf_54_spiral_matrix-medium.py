# doesn't work... wrong 

# class Solution:
#     def spiralOrder(self, matrix):
#         if not matrix or not matrix[0]:
#             return []
#         ret = []
#         n, m = len(matrix), len(matrix[0])
#         for i in range(math.ceil(min(n, m) / 2)):
#             ret.extend(self.onePath(matrix, i))
#         return ret

#     def onePath(self, matrix, idx):
#         ret = []
#         n, m = len(matrix), len(matrix[0])
#         for i in range(idx, m - idx):
#             ret.append(matrix[idx][i])

#         for i in range(idx + 1, n - idx):
#             ret.append(matrix[i][m-1-idx])
#         for i in range(m - idx - 2, -1+idx, -1):
#             ret.append(matrix[n-1-idx][i])
#         for i in range(n - idx - 2, 0+idx, -1):
#             ret.append(matrix[i][idx])
#         return ret


# solution 1... still don't quite understand
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        row_start, row_end, col_start, col_end = 0, m - 1, 0, n - 1
        result = []
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            
            if row_start <= row_end: #@ error, missing this one causing erraneous behavior
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            
            if col_start <= col_end: #@ error, missing this one causing erraneous behavior
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
                
        return result
