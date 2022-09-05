class Solution(object):
    def largestRectangleArea(self, heights):
        stack=[]
        maxArea=0
        for ind, val in enumerate(heights):
            temp=ind
            while stack and val < stack[-1][1]:
                cind, cval = stack.pop()
                maxArea=max(maxArea, (ind-cind)*cval)
                temp=cind
            stack.append([temp, val])
        
        last=len(heights)
        while stack:
            ind, val =stack.pop()
           
            maxArea=max(maxArea, (last-ind)*val)
        return maxArea
    
    
#     maxArea = 0
#         stack = []  # pair: (index, height)

#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))

#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea
        