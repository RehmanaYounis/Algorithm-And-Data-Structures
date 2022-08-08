class TimeMap(object):

    def __init__(self):
        self.store={}

    def set(self, key, value, timestamp):
        if not key in self.store:
            self.store[key]=[]
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        res=''
        values=self.store.get(key,[])
        l=0 ; r = len(values)-1
        while l<=r:
            mid = (l+r)//2
            if timestamp < values[mid][1]:    
                r=mid-1
            else:
                res=values[mid][0]
                l=mid+1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)