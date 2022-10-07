# https://www.youtube.com/watch?v=SA867FvqHrM

class Solution(object):
    def rotate(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        
        for i in range(rows):
            l=0; r = cols-1
            while l<r:
                matrix[i][l], matrix[i][r]= matrix[i][r], matrix[i][l]
                l+=1
                r-=1
        
        return matrix
        