# https://www.youtube.com/watch?v=SA867FvqHrM

class Solution(object):
    def rotate(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        
        row_start=0
        col_start=0
        
        for i in range(rows):
            for j in range(i, cols):
                temp =matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i]=temp
        
        for i in range(rows):
            l, r= 0, cols-1
            while l<r:
                temp=matrix[i][l]
                matrix[i][l]=matrix[i][r]
                matrix[i][r] = temp
                l+=1
                r-=1
                
                
                
        
        return matrix
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         rows=len(matrix)
#         cols=len(matrix[0])
#         for i in range(rows):
#             for j in range(i, cols):
#                 matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        
#         for i in range(rows):
#             l,r=0,cols-1
#             r = cols-1
#             while l<r:
#                 matrix[i][l], matrix[i][r]= matrix[i][r], matrix[i][l]
#                 l+=1
#                 r-=1
        
#         return matrix
        