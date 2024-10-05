class MedianFinder:

    def __init__(self):
        self.left,self.right=[],[]
        

    def addNum(self, num: int) -> None:
        if self.right and num>self.right[0]:
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left, -num)
        
        if len(self.left)>len(self.right)+1:
            val=-1* heappop(self.left)
            heapq.heappush(self.right,val)
        
        elif len(self.right) > len(self.left)+1:
            val=-1 * heappop(self.right)
            heapq.heappush(self.left,val)

        

#         elif len(self.large)> len(self.small)+1:
#             val=heapq.heappop(self.large)
#             heapq.heappush(self.small, (-1 * val))
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            val1=-1 * self.left[0]
            val2= self.right[0]
            return (val1+val2)/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()