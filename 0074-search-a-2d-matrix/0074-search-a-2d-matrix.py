class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS=len(matrix)
        COLS=len(matrix[0])
        begin=0
        end=ROWS-1
        
        while begin<=end:
            mid=(begin+end)//2
            if target>matrix[mid][-1]:
                begin=mid+1
            elif target<matrix[mid][0]:
                end=mid-1
            else:
                break
        row=mid
        print(row)
        left=0
        right=COLS-1
        while left<=right:
            mid=(left+right)//2
            if matrix[row][mid] < target:
                left=mid+1
            elif matrix[row][mid] > target:
                right=mid-1
            else:
                return True
        return False
 
        
         