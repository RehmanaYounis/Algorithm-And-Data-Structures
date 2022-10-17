class Solution(object):
    def coinChange(self, coins, amount):
        if amount==0: return 0
        hashMap={0:0}
        def dfs(curVal):
            if curVal==0:
                return 0
            if curVal<0:
                return -1
            if curVal in hashMap:    
                return hashMap[curVal]
            curShort=float('inf')
            for i in coins:
                res = dfs(curVal-i)
                if res != -1:
                    cur = res +1
                    curShort=min(curShort, cur)
                
            
            hashMap[curVal]=curShort
            return hashMap[curVal]
           

            
        minVal= dfs(amount)
        if minVal != float('inf'):    return minVal
        else: return -1
        