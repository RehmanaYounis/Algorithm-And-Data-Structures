class Solution(object):
    def merge(self, intervals):
      
        intervals.sort(key=lambda i:i[0])
        res=[intervals[0]]
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_start=intervals[i][0]
            cur_end=intervals[i][1]
            
            if prev < cur_start:
                res.append([cur_start,cur_end])
            else:
                res[-1][1]=max(cur_end,prev )
                
            prev=max(prev, cur_end)
            
        return res
            
                
                