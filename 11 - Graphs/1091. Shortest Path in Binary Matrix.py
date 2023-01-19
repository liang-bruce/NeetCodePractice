class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        # BFS for shortest path
        def bfs():
            if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1:
                return -1
            
            q = deque()
            visited.add((0,0))
            q.append((0,0,1))

            while q:
                curR, curC, length = q.popleft()

                if curR == ROW - 1 and curC == COL - 1:
                    return length

                directions = [[0,1], [0,-1],[1,0],[-1,0],
                                [1,1],[-1,-1],[1,-1],[-1,1]]
                for dr, dc in directions:
                    r, c = curR + dr, curC + dc
                    if (r in range(ROW) and 
                        c in range(COL) and
                        grid[r][c] == 0 and
                        (r,c) not in visited):
                        q.append((r, c, length + 1))
                        visited.add((r,c))
            
            return -1
        
        res = bfs()

        return res 