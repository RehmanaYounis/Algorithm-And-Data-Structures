class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output=[]
        l=0
        q=collections.deque()
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l> q[0]:
                q.popleft()
            if (r+1)>= k:
                output.append(nums[q[0]])
                l+=1
        return output