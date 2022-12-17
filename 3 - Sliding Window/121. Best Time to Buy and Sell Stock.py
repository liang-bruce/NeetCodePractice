class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPtr, sellPtr = 0, 1
        result = 0
        while buyPtr < len(prices) and sellPtr < len(prices):
            
            if prices[buyPtr] >= prices[sellPtr]:
                buyPtr = sellPtr
                # sellPtr += 1
            else:
                currProfit = prices[sellPtr] -prices[buyPtr]
                result = max(result, currProfit)
                # sellPtr += 1
                
            sellPtr += 1

        return result