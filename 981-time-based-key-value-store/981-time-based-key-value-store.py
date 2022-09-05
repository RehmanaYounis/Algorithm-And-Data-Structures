class TimeMap(object):

    def __init__(self):
        self.TimeStamp={}

    def set(self, key, value, timestamp):
        if key not in self.TimeStamp:
            self.TimeStamp[key]=[]
        self.TimeStamp[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        res, values = "", self.TimeStamp.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)