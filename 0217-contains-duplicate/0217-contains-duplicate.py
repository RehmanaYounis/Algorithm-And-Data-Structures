class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nmap=defaultdict(int)
        for num in nums:
            if nmap[num] == 1:
                return True
            nmap[num]=1
        return False
        