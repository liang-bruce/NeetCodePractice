class Solution:
    def minSwaps(self, s: str) -> int:
        # tips: 1 operation cancels (neutralize) 2 "]"
        # find the max num of unopened "]" then (max + 1) // 2
        maxUnopened, curUnopened = 0, 0

        for c in s:
            if c == ']':
                curUnopened += 1
            else:
                curUnopened -= 1
            
            maxUnopened = max(curUnopened, maxUnopened)
        
        return (maxUnopened + 1) // 2 # 1 operation cancels (neutralize) 2 "]"