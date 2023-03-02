class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # def recursion(day):
        #     if day == len(prices) - 1:
        #         return 0
            
        #     maxCurr = max(prices[day + 1] - prices[day], 0)
        #     maxNext = recursion(day + 1)
        #     return maxCurr + maxNext
        
        # res = recursion(0)

        # return res

        # sliding window with fixed size: 1
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        
        return res