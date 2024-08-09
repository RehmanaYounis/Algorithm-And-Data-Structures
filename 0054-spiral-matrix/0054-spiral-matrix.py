class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start=0
        rows= len(matrix)
        col_start =0
        cols = len(matrix[0])
        
        res=[]
        while row_start < rows and col_start <cols:
            for c in range(col_start, cols):
                res.append(matrix[row_start][c])
        
            row_start+=1
         
            for r in range(row_start, rows):
                res.append(matrix[r][cols-1])
            cols-=1
            
            if row_start < rows:
                for c in range(cols-1, col_start-1, -1):
                    res.append(matrix[rows-1][c])
                rows-=1
            if col_start<cols:
                for r in range(rows-1, row_start-1, -1):
                    res.append(matrix[r][col_start])
                col_start+=1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         rowStart=0
#         colStart=0
#         rowEnd=len(matrix)
#         colEnd=len(matrix[0])
        
#         res=[]
        
#         while rowStart< rowEnd and colStart< colEnd:
            
#             for col in range(colStart,colEnd):
                
#                 res.append(matrix[rowStart][col])
            
#             rowStart+=1
#             for row in range(rowStart, rowEnd):     
#                 res.append(matrix[row][colEnd-1])
#             colEnd-=1
            
#             if rowStart< rowEnd:
#                 for col in range(colEnd-1, colStart-1, -1):
#                     res.append(matrix[rowEnd-1][col])
            
#             rowEnd-=1
#             if colStart<colEnd:
#                 for row in range(rowEnd-1, rowStart-1, -1):
#                     res.append(matrix[row][colStart])
#             colStart+=1        
#         return res