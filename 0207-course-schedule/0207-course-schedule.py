class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap=defaultdict(list)
        for crs, pre in prerequisites:
            hashMap[crs].append(pre)
        visit=[]
        def dfs(crs):
            if crs in visit:
                return False
            if hashMap[crs]==[]:
                return True
            visit.append(crs)
            for pre in hashMap[crs]:
                if not dfs(pre): 
                    return False
            visit.pop()
            hashMap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True