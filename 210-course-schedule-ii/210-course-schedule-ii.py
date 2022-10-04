class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cMap={}
        for i in range(numCourses):
            cMap[i]=[]
        for crs, pre in prerequisites:
            cMap[crs].append(pre)
        visit=set()
        res=[]
        cycle=set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in cMap[course]:
                if not dfs(pre): 
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
                
                
              
            
        
        for crs in range(numCourses):
            if not dfs(crs): return []
                
        return res