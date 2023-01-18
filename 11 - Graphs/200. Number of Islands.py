class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # recursive DFS
        island = 0
        visit = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(ROW) or 
                c not in range(COL) or
                (r, c) in visit or
                grid[r][c] == "0"):
                return
            
            visit.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    island += 1
        
        return island

# BFS Version From Video
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

         def bfs(r,c):
             q = deque()
             visited.add((r,c))
             q.append((r,c))
           
             while q:
                 row,col = q.popleft() # change this line to row,col = q.pop() will make this code iterative DFS
                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                 for dr,dc in directions:
                     r,c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                         q.append((r , c ))
                         visited.add((r, c ))

         for r in range(rows):
             for c in range(cols):
               
                 if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)
                     islands +=1 

         return islands
