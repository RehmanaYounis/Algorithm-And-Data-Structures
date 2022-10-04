class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cMap={i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            cMap[crs].append(pre)
        
        visit=set()
        
        def dfs(course):
            if course in visit:
                return False
            if cMap[course]==[]:
                return True
            visit.add(course)
            for pre in cMap[course]:
                if not dfs(pre):
                    return False
            cMap[course]=[]
            visit.remove(course)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
    
   