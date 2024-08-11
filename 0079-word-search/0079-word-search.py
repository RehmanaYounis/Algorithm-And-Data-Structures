class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visit=[]
        
        def dfs(r,c,i):
            if i ==len(word):
                return True
            if r<0 or r == rows or c < 0 or c == cols or [r,c] in visit or board[r][c] != word[i]:
                return False
            visit.append([r,c])
            
            if dfs(r+1, c , i+1): return True
            if dfs(r-1, c , i+1):return True
            if dfs(r, c+1 , i+1):return True
            if  dfs(r, c-1 , i+1):return True
                
            visit.pop()
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0) == True:
                    return True
        return False