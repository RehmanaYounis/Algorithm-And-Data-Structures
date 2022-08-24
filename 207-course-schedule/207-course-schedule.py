class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap={i:[] for i in range((numCourses))}
        for crs,pre in prerequisites:
            cmap[crs].append(pre)
        print(cmap)
        visited=set()
        def dfs(cur):
            if cur in visited:
                return False
            if cmap[cur]==[]:
                return True
            visited.add(cur)
            for pre in cmap[cur]:
                if not dfs(pre): return False
            visited.remove(cur)
            cmap[cur]=[]
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True