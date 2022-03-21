import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        rows=len(grid)
        cols =len(grid[0])
        output=grid#np.ones((rows, cols), int)
        for i in range(1, cols):
            output[0][i]=output[0][i-1] + grid[0][i]
            
        for i in range(1, rows):
            output[i][0]=output[i-1][0] + grid[i][0]
        
        for i in range(1, rows):
            for j in range(1,cols):
                output[i][j]=min(output[i-1][j],output[i][j-1])+grid[i][j]
        
#         print(output)
#         print(grid[rows-1][cols-1])
        return(output[rows-1][cols-1])
        
            
        