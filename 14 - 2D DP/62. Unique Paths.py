class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # #dp
        # preRow = [0] * n

        # for i in range(m):
        #     curRow = [0] * n
        #     curRow[n - 1] = 1

        #     for j in range(n - 2, -1, -1):
        #         curRow[j] = preRow[j] + curRow[j + 1]
            
        #     preRow = curRow
        
        # return preRow[0]

        # memoization

        def memo(r, c, cache):
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 or c == n - 1:
                return 1
            
            cache[r][c] = memo(r + 1, c, cache) + memo(r, c + 1, cache)

            return cache[r][c]

        return memo(0,0,[[0] * n for _ in range(m)])