class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visit=set()
        directions=[[-1,0], [1,0], [0,-1], [0,1]]
        def dfs(i, r, c):
            if i==len(word):
                return True
            if r<0 or r>rows-1 or c <0 or c>=cols or r>=rows or board[r][c] != word[i] or (r,c) in visit:
                return 
            
            visit.add((r,c))
            for cr,cc in directions:
                nr=cr+r
                nc=cc+c
                if dfs(i+1, nr,nc):return True
            visit.remove((r,c))
            return False
           
        
        
        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        return False
            
            
            
            
            
            