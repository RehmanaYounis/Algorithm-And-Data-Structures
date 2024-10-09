class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap=defaultdict(list)
        for key,val in prerequisites:
            preMap[key].append(val)
        visited=[]
        def dfs(crs):
            if preMap[crs]==[]:
                return True
            if crs in visited:
                return False
            visited.append(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            visited.pop()
            preMap[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        