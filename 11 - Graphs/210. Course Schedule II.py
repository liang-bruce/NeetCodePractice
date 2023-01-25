class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adjList[course].append(pre)

        res = []
        visited, studied = set(), set()
        def dfs(i):
            if i in studied:
                return True
            if i in visited:
                return False
            
            visited.add(i)
            for course in adjList[i]:
                if not dfs(course):
                    return False
            visited.remove(i)
            studied.add(i)
            res.append(i)

            return True
        
        for course in adjList.keys():
            if not dfs(course):
                return []
        return res