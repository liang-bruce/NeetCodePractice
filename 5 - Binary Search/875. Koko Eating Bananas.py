class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on [1...max(piles)], update l when totalTime > h, update r and result when totalTime <= h
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            curSpeed = (l + r) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / curSpeed)
            
            if totalTime <= h:
                res = min(res,curSpeed)
                r = curSpeed - 1
            else:
                l = curSpeed + 1
        
        return res