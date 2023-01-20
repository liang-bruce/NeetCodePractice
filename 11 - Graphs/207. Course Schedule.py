class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            adjMap[course].append(pre)

        visited = set()
        def dfs(i):
            if adjMap[i] == []:
                return True
            if i in visited:
                return False
            
            visited.add(i)
            for c in adjMap[i]:
                if not dfs(c):
                    return False
            visited.remove(i)
            # clear adjMap[i] cos it can be finished
            adjMap[i] = []
            return True
        for i in adjMap.keys():
            if not dfs(i):
                return False
        
        return True