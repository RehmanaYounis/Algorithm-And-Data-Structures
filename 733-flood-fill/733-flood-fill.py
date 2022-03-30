class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        
        directions=[[1,0],
                    [-1,0],
                    [0,1],
                    [0,-1]]
        rows=len(image)
        cols=len(image[0])
        q=deque()

        q.append([sr,sc])
        color=image[sr][sc]
        if color==newColor: return image
        while q:
            val=q.popleft()
            row=val[0]
            col=val[1]
            image[row][col]=newColor
            for dir1 in directions:
                new_r=row+dir1[0]
                new_c=col+dir1[1]
                if new_r>=0 and new_c>=0 and new_r<rows and new_c<cols and image[new_r][new_c]==color:
                    q.append([new_r,new_c])
        return image
            