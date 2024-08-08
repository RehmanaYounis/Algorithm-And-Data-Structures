class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length=len(matrix)
        for i in range(length):
            for j in range(i, length):
                temp=matrix[i][j]
                matrix[i][j]= matrix[j][i]
                matrix[j][i]= temp
        
        for i in range(length):
            l,r=0,length-1
            while l<r:
                temp1=matrix[i][l]
                matrix[i][l]=matrix[i][r]
                matrix[i][r]=temp1
                l+=1
                r-=1
            