class Solution(object):
    def searchMatrix(self, matrix, target):
        ROWS=len(matrix)
        COLS=len(matrix[0])
        top=0
        bottom=ROWS -1
        while top<=bottom:
            row=(top+bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break
            print(top, bottom, row)
        
        l=0 ; r =COLS-1
        while l<=r:
            mid=(l+r)//2
            if target==matrix[row][mid]:
                return True
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                r=mid-1
        return False

  