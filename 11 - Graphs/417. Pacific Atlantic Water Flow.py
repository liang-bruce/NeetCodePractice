class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # start from edges, go backwards to find which cell can flow in to pac / atl, then find common cells
        ROW, COL = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r not in range(ROW) or
                c not in range(COL) or
                (r, c) in visited or
                heights[r][c] < prevHeight):
                return 

            visited.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        # start from top and bottom    
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, atl, heights[ROW - 1] [c])

        # start from left and right
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL - 1])

        # find common (r,c)
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res