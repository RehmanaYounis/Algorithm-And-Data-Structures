# Step 1: Checking base condition if matrix not startting from 0, return -1
# Step 2: Calculate number of rows, columns
# Step 3: Create an empty que
# Step 4: Append for initial element , (0,0, 1) for x , y and step count
# Step 5: Update value of 0th position with 1
# Step 6: Create Direction Array
# Step 7: Check if que not empty
# Step 8: Execute for loop till length of que
# Step 9: pop left que element
# Step 10: If position of point is last element of matrix and value is 0, return step count
# Step 11: Execute for in all direction array:
# Step 12: commute row and column updated value
# Step 13: If row and column values are valid and the value of cell is zero add element to que

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0]==1: return -1
        rows=len(grid)
        cols = len(grid[0])
        directions =[[0,1],
                    [0,-1],
                    [1,0],
                    [-1,0],
                    [1,1],
                    [1,-1],
                    [-1,1],
                    [-1,-1]]
        que=deque()
        grid[0][0]=1
        que.append([0,0,1])
        print(que)
        while que:
            cur_left, cur_right, cur_count = que.popleft()
            if cur_left == rows-1 and cur_right== cols -1 :
                return cur_count
            
            for d in directions:
                new_left=cur_left + d[0]
                new_right = cur_right +d[1]
                if new_left >= 0 and new_right>=0 and new_left<rows and new_right<cols and grid[new_left][new_right] == 0:
                    grid[new_left][new_right]  = 1
                    que.append([new_left, new_right, cur_count+1])
        return -1
