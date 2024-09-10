class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(i, cols):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        
        for row in range(rows):
            left=0
            right=cols-1
            while left < right:
                temp=matrix[row][left]
                matrix[row][left]=matrix[row][right]
                matrix[row][right]=temp
                left+=1
                right-=1
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         length=len(matrix)
#         for i in range(length):
#             for j in range(i, length):
#                 temp=matrix[i][j]
#                 matrix[i][j]= matrix[j][i]
#                 matrix[j][i]= temp
        
#         for i in range(length):
#             l,r=0,length-1
#             while l<r:
#                 temp1=matrix[i][l]
#                 matrix[i][l]=matrix[i][r]
#                 matrix[i][r]=temp1
#                 l+=1
#                 r-=1
            