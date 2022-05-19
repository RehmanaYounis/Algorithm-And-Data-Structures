class Solution(object):
    def isValidSudoku(self, board):
         
        for i in range(9):
            hashmap={}
            for j in range(9):
                val=board[i][j]
                
                if val in hashmap.keys() and val !='.':
                    return False
                else:
                    hashmap[val]=True
                    
        for i in range(9):
            hashmap={}
            for j in range(9):
                val=board[j][i]
                if val in hashmap.keys() and val !='.':
                    return False
                else:
                    hashmap[val]=True
            
        hashmap=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                key=(i//3, j//3)
                if val =='.':
                    continue
                if val in hashmap[key] :
                    return False
                else:
                    hashmap[key].add(val)
        return True 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         rowsDict= collections.defaultdict(set)
#         colsDict= collections.defaultdict(set)
#         squareDict=collections.defaultdict(set)
        
#         for r in range(9):
#             for c in range(9):
#                 val=board[r][c]
#                 if val=='.':
#                     continue
#                 if (val in rowsDict[r] or  
#                     val in colsDict[c] or 
#                     val  in squareDict[(r//3,c//3)]):
#                      return False
#                 rowsDict[r].add(val)
#                 rowsDict[c].add(val)
#                 squareDict[(r//3, c//3)].add(val)
                
                   
#         return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     