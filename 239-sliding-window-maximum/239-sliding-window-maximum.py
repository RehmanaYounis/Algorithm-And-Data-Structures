class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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






