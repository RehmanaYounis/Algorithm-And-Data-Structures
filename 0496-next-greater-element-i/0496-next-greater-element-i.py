class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[nums2[0]]
        hashMap={}
        for i in nums2:
            while stack and i>stack[-1]:
                temp=stack.pop()
                hashMap[temp]=i
            stack.append(i)
        print(hashMap)
        res=[]
        for i in nums1:
            if i in hashMap:
                res.append(hashMap[i])
            else:
                res.append(-1)
        return res