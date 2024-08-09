class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        
        def dfs(r,c,dire):
            if r <0 or r>=rows or c < 0 or c>=cols or matrix[r][c] == 0:
                return
            matrix[r][c] = '*'
            if dire=='U':
                dfs(r-1,c,'U')
            if dire=='D':
                dfs(r+1,c,'D')
            if dire=='L':
                dfs(r,c-1,'L')
            if dire=='R':
                dfs(r,c+1,'R')
                
        for r in range(rows):
            for c in range (cols):
                if matrix[r][c] == 0:
                    dfs(r-1,c,'U')
                    dfs(r+1,c,'D')
                    dfs(r,c-1,'L')
                    dfs(r,c+1,'R')
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=='*':
                    matrix[r][c]=0
        return matrix
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ROWS= len(matrix)
#         COLS=len(matrix[0])
#         visit=set()
#         def dfs(r,c,dire):
#             if r<0 or r>=ROWS or c<0 or c>= COLS  or matrix[r][c] == 0:
#                 return
#             matrix[r][c]='*'
#             if dire == 'U':
#                 dfs(r-1, c, 'U')
#             elif dire == 'D':
#                 dfs(r+1, c, 'D')
#             elif dire =='R':
#                 dfs(r, c+1,'R')
#             else:
#                 dfs(r, c-1,'L')
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if matrix[r][c]==0:
#                     dfs(r+1,c, 'D')
#                     dfs(r-1,c, 'U')
#                     dfs(r,c-1, 'L')
#                     dfs(r,c+1, 'R')
        
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if matrix[r][c]=='*':
#                     matrix[r][c]=0
                    
#         return matrix
        