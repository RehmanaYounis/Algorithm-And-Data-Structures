class Solution(object):
    def circularArrayLoop(self, nums):
        def getNext(index, direction):
            curDirection=nums[index]>0
            if curDirection != direction:
                return -1
            curIndex=(index+nums[index])%len(nums)
            if curIndex<0:
                curIndex+=len(nums)
            if curIndex==index:
                return -1
            return curIndex
        
        
        
        
        
        for i in range(len(nums)):
            slow= fast = i
            direction = nums[i]>0
            while True:
                slow= getNext(slow, direction)
                if slow == -1:
                    break
                fast= getNext(fast, direction)
                if fast == -1:
                    break
                fast= getNext(fast, direction)
                if fast == -1:
                    break
                if slow == fast:
                    return True
        return False
    