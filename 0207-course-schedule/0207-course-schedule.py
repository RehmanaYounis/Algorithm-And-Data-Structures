class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap=defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit=set()
        def dfs(crs):
            if preMap[crs]==[]:
                return True
            if crs in visit:
                return False
            visit.add(crs)
            for cs in preMap[crs]:
                if not dfs(cs):
                    return False
            preMap[crs]=[]
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        