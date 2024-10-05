class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        crsMap=defaultdict(list)
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if crsMap[crs]==[]:
                return True
            visited.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            crsMap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         preMap=defaultdict(list)
#         for crs, pre in prerequisites:
#             preMap[crs].append(pre)
        
#         visit=set()
#         def dfs(crs):
#             if preMap[crs]==[]:
#                 return True
#             if crs in visit:
#                 return False
#             visit.add(crs)
#             for cs in preMap[crs]:
#                 if not dfs(cs):
#                     return False
#             preMap[crs]=[]
#             return True
        
        
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False
#         return True

        