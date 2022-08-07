class Solution(object):
    def exist(self, board, word):
        rows=len(board)
        cols=len(board[0])
        visited=set()
        def dfs(r, c, j):
            if j==len(word):
                return True
            if (r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or word[j]!= board[r][c]):
                return False
            visited.add((r,c))
            res=(dfs(r+1, c, j+1) or 
                 dfs(r-1, c, j+1) or 
                 dfs(r, c+1, j+1) or 
                 dfs(r, c-1, j+1)       
                )
            visited.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if (dfs(r,c,0)):
                    return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         rows= len(board)
#         columns=len(board[0])
       
#     #DFS Function
#         def dfs(board, word, i, j):
#             if len(word)==0: return True
            
#             if i<0 or i>=rows or j<0 or j>=columns or board[i][j]!=word[0] or board[i][j]=='*': return False
            
#             c= board[i][j]
#             board[i][j]='*'
#             word=word[1:]
#             res = dfs(board, word, i-1, j) or dfs(board, word, i+1, j) or  dfs(board, word, i, j-1) or dfs(board,                       word, i, j+1)
#             board[i][j] =c
#             return res
        
#         # Matrix Cells Traversal
#         for r in range(rows):
#             for c in range(columns):
#                 if (board[r][c] == word[0]) and dfs(board, word, r,c):
#                     return True
#         return False
                    
                    
                    
                    
                