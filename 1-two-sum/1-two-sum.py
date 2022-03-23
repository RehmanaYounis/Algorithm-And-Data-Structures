class Solution(object):
    def twoSum(self, nums, target):
        friend_map ={}
        for i in range (len(nums)):
            if nums[i] not in friend_map:
                friend_map[target-nums[i]]=i
            else:
                return [friend_map[nums[i]], i]