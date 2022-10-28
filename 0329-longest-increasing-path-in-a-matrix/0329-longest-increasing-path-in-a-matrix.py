class Solution(object):
    def longestIncreasingPath(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        maxPath=0
        dp={}
        def dfs(r,c, visit,prev):    
            if (r,c,prev) in dp:
                return dp[(r,c,prev)]
            if r<0 or r>=rows or c<0 or c>=cols or [r,c] in visit or matrix[r][c]<=prev:
                return 0
            visit.append([r,c])
            right=dfs(r+1,c,visit,matrix[r][c])
            left=dfs(r-1,c,visit,matrix[r][c])
            down=dfs(r,c+1,visit,matrix[r][c])
            bottom=dfs(r,c-1,visit,matrix[r][c])
            visit.pop()
            dp[(r,c,prev)]=1+max(right,left,down,bottom)
            return dp[(r,c,prev)]
        
        for i in range(rows):
            for j in range(cols):
                maxPath=max(maxPath,dfs(i,j,[],float('-inf')))
        return maxPath