class Solution:
    def arrangeCoins(self, n: int) -> int:
        # O(n)
        # if n <= 2:
        #     return 1
        # for i in range(1, n):
        #     if n - i > 0:
        #         n = n - i
        #     elif  n - i == 0:
        #         return i
        #     else:
        #         return i - 1
        
        # O(log(n))
        l, r = 1, n
        res = 0
        while l <= r:
            mid = (l+r) // 2
            coinsRequired = (mid / 2) * (mid + 1) # Gauss formula
            if coinsRequired > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res

        # O(1) Gauss Formula mathematically
        # res = (-1 + sqrt(1 + 8 * n)) / 2
        # return math.floor(res)