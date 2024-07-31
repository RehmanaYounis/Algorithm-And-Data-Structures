class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap=defaultdict(list)
        visit=[]
        for crs, pre in prerequisites :
            hashMap[crs].append(pre)
        
        
        def dfs(course):
            if course in visit: return False
            
            if hashMap[course]==[]:
                return True
            visit.append(course)
            for pre in hashMap[course]:
                if not dfs(pre): return False
            hashMap[course]=[]
            visit.pop()
            return True
        
        
        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True
        
                
#         hashMap=defaultdict(list)
#         for crs, pre in prerequisites:
#             hashMap[crs].append(pre)
#         visit=[]
#         def dfs(crs):
#             if crs in visit:
#                 return False
#             if hashMap[crs]==[]:
#                 return True
#             visit.append(crs)
#             for pre in hashMap[crs]:
#                 if not dfs(pre): 
#                     return False
#             visit.pop()
#             hashMap[crs]=[]
#             return True
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hashMap=defaultdict(list)
#         for crs, pre in prerequisites:
#             hashMap[crs].append(pre)
#         visit=[]
#         def dfs(crs):
#             if crs in visit:
#                 return False
#             if hashMap[crs]==[]:
#                 return True
#             visit.append(crs)
#             for pre in hashMap[crs]:
#                 if not dfs(pre): 
#                     return False
#             visit.pop()
#             hashMap[crs]=[]
#             return True
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False
#         return True
    
    
    