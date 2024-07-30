class MedianFinder:
    def __init__(self):
        self.small,self.large=[],[]
        

    def addNum(self, num: int) -> None:
        if self.large and num>self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small, (-1 * num))
        if len(self.small)> len(self.large)+1:
            val=-1* heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        elif len(self.large)> len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small, (-1 * val))



#         if len(self.small) > len(self.large) + 1:
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)
#         if len(self.large) > len(self.small) + 1:
#             val = heapq.heappop(self.large)
#             heapq.heappush(self.small, -1 * val)       
            
            
            
            
    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            val = -1 * self.small[0]
        elif len(self.large)>len(self.small):
            val = self.large[0]
        else:
            v1=-1 * self.small[0]
            v2= self.large[0]
            val=(v1+v2)/2
        return val

       
    
    
    
    
    
    
    
    
    
    