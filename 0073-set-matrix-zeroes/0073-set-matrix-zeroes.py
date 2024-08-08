class Solution(object):
    def setZeroes(self, matrix):
        rows, cols=len(matrix), len(matrix[0])
        
        def dfs(r,c,dir):
            if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c]== 0:
                return
            matrix[r][c]='*'
            if dir=='U':
                dfs(r-1,c,'U')
            if dir=='D':
                dfs(r+1,c,'D')
            if dir=='L':
                dfs(r,c-1,'L')
            if dir=='R':
                dfs(r,c+1,'R')
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    dfs(r-1,c,'U')
                    dfs(r+1,c,'D')
                    dfs(r,c-1,'L')
                    dfs(r,c+1,'R')
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=='*':
                    matrix[r][c]=0
        return matrix
                    