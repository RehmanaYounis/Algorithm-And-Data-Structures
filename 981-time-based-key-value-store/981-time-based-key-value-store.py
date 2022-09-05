class TimeMap(object):

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        res=""
        values=self.store[key]
        l, r = 0 , len(values)-1
        while l <= r:
            mid = (l + r)//2
            if  values[mid][1] <= timestamp:
                res=values[mid][0]
                l= mid+1
            else:
                r = mid - 1
        return res
    
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)