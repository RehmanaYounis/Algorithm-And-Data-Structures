class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cmap={i:[] for i in range(numCourses)}
        visited=set()
        cycle=set()
        output=[]
        for cr,pre in prerequisites:
            cmap[cr].append(pre)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in cmap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            output.append(crs)
            visited.add(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):return []
        return output
        