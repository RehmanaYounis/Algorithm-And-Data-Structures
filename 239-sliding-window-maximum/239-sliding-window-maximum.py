class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res=[]
        for ind , val in enumerate(nums):
            while q and val>=nums[q[-1]]:
                q.pop()
            q.append(ind)
            if q[0]==ind-k:
                q.popleft()
            if ind >=k-1:
                res.append(nums[q[0]])
        return res



























