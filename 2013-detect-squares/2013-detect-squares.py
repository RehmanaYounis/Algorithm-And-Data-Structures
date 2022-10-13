class DetectSquares:

    def __init__(self):
        self.pmap=defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        x,y=point
        self.pmap[tuple((x,y))]+=1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        count=0
        for x,y in self.pts:
            if qx==x and qy==y or abs(qx-x)!= abs(qy-y):
                continue
            
           
            count+= self.pmap[(x,qy)] * self.pmap[(qx,y)]
        return count

    
    
# def __init__(self):
#         self.ptsCount = defaultdict(int)
#         self.pts = []

#     def add(self, point: List[int]) -> None:
#         self.ptsCount[tuple(point)] += 1
#         self.pts.append(point)

#     def count(self, point: List[int]) -> int:
#         res = 0
#         px, py = point
#         for x, y in self.pts:
#             if (abs(py - y) != abs(px - x)) or x == px or y == py:
#                 continue
#             res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
#         return res


    

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)