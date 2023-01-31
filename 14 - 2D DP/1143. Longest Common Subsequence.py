class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # bottom up
        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[0][0]

        # memo TLE
        # create grid:
        row, col = len(text1), len(text2)
        grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        def memo(i, j):
            nonlocal grid
            if i > row - 1 or j > col - 1:
                return 0
            if text2[j] == text1[i]:
                grid[i][j] = 1 + memo(i + 1, j + 1)
                return grid[i][j]
            else:
                grid[i][j] = max(memo(i + 1, j), memo(i, j + 1))
                return grid[i][j]
        
        memo(0, 0)
        # print(grid)
        return grid[0][0]