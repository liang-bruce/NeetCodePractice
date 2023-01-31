class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # memo
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # if obstacleGrid[m - 1][n - 1] == 1:
        #     return 0

        # def memo(r, c, cache):
        #     if r == m or c == n or obstacleGrid[r][c] == 1:
        #         return 0
        #     if cache[r][c] > 0:
        #         return cache[r][c]
        #     if r == m - 1 and c == n - 1:
        #         return 1
            
        #     cache[r][c] = memo(r + 1, c, cache) + memo(r, c + 1, cache)
        #     # print(cache)
        #     return cache[r][c]
        # # print(cache)
        # return memo(0,0,[[0] * n for _ in range(m)])

        # bottom up
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        preRow = [0] * col

        for r in range(row - 1, -1, -1):
            curRow = [0] * col
            if r == row - 1 and obstacleGrid[r][col - 1] == 0:
                curRow[col - 1] = 1
            if r < row - 1:
                curRow[col - 1] = 1 if preRow[col - 1] == 1 and obstacleGrid[r][col - 1] == 0 else 0

            for c in range(col - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] = preRow[c] + curRow[c + 1]
            preRow = curRow
            print(preRow)

        return preRow[0]
