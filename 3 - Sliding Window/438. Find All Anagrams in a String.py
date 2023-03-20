class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = Counter(p)
        
        L = len(p)
        l, r = 0, 0
        res = []
        # print(pDict)
        while l <= len(s) - L and r < len(s):
            # print(l, pDict)
        
            while r < len(s) and r - l < L:
                if s[r] in pDict:
                    pDict[s[r]] -= 1 
                r += 1
            
            if all(value == 0 for value in pDict.values()):
                res.append(l)
            
            if s[l] in pDict:
                pDict[s[l]] += 1
            l += 1
            # print(l, pDict)
        return res