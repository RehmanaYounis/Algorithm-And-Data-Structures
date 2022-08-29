class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left , -num)
        if self.left and self.right and -(self.left[0]) > self.right[0]:
            heapq.heappush(self.right, -(heapq.heappop(self.left)))
        if len(self.left)>len(self.right)+1:
            heapq.heappush(self.right, -(heapq.heappop(self.left)))
           
        if len(self.right)>len(self.left)+1:
             heapq.heappush(self.left, -(heapq.heappop(self.right)))
        
        
        
        


    def findMedian(self) -> float:
        if len(self.left)> len(self.right):
            return - self.left[0]
        elif len(self.right)> len(self.left):
            return self.right[0]
        else:
            med = ((-self.left[0])+(self.right[0]))/2
        return med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()