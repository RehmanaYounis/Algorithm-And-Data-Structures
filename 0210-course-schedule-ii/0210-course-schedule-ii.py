class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap=defaultdict(list)
        for crs , pre in prerequisites:
            preMap[crs].append(pre)
        
        visit=set()
        cycle=[]
        output=[]
        
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.append(crs)
            for cs in preMap[crs]:
                if not dfs(cs):
                    return False
            visit.add(crs)
            cycle.pop()
            output.append(crs)
            return True
        
        
        for cs in range(numCourses):
            if not dfs(cs):
                return []
        return output