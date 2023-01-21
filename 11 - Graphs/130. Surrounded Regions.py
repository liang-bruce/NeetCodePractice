class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        cap, notCap = set(), set()
        
        def dfs(r, c):
            if (r not in range(ROW) or 
                c not in range(COL) or
                board[r][c] == "X" or 
                (r, c) in notCap):
                return
            # print("in dfs", r, c)
            if (r, c) in cap:
                cap.remove((r, c))
                # print("moved")
            notCap.add((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # run dfs on all border "O" 
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    # check if (r,c) is on border
                    if (r == 0 or r == ROW - 1 or
                        c == 0 or c == COL - 1):
                        dfs(r, c)
                    else:
                        if (r, c) not in notCap:
                            cap.add((r,c))

        for r, c in cap:
            board[r][c] = "X" 