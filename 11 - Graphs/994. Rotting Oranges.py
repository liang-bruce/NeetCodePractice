class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        rotted, fresh = set(), set()
        minTime = 0

        # bfs function for spreading 
        def bfs():
            time = 0
            q = deque()
            for r, c in rotted:
                q.append((r, c, time))
            
            while q:
                preRow, preCol, time = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for rd, cd in directions:
                    row, col = preRow + rd, preCol + cd
                    if (row in range(ROW) and 
                        col in range(COL) and
                        grid[row][col] == 1 and 
                        (row, col) not in rotted):
                        rotted.add((row,col))
                        q.append((row, col, time + 1))

                        if (row, col) in fresh:
                            fresh.remove((row, col))
            return time

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    rotted.add((r, c))

                if grid[r][c] == 1:
                    fresh.add((r, c))
        
        minTime = bfs()
        
        if len(fresh):
            return -1
        else:
            return minTime