class Solution(object):
    def exist(self, board, word):
        rows=len(board)
        cols=len(board[0])
        visit=[]
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c, i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or board[r][c] != word[i]):
                return 
            
            visit.append((r,c))
            for cr,cc in direction:
                nr=r+cr
                nc=c+cc
                if dfs(nr,nc,i+1):return True
            visit.pop()
            
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False
                