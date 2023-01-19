class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        visited = set()

        # recursive DFS
        def dfs(r, c):
            size = 1
            if (r not in range(len(grid)) or
                c not in range(len(grid[0])) or
                grid[r][c] == 0 or
                (r,c) in visited):
                return 0
                
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in directions:
                size += dfs(r + dr, c + dc)

            return size
        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curSize = dfs(r, c)
                    maxSize = max(curSize, maxSize)
        
        return maxSize