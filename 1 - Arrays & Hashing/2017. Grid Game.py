class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()

        # calculate 2 prefic rows
        for i in range(1, N):
            preRow1[i] += preRow1[i - 1]
            preRow2[i] += preRow2[i - 1]
        
        res = float("inf")
        # i is the "turning point" of the 1st robot
        for i in range(N):
            top = preRow1[-1] - preRow1[i]
            bottom = 0 if i == 0 else preRow2[i - 1]
            secondRobot  = max(top, bottom)
            res = min(res, secondRobot)
        
        return res