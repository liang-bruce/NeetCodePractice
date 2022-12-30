class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = 0
        scharMap = {}
        tcharMap = {}

        while i < len(s):
            if (s[i] in scharMap and scharMap[s[i]] != t[i]) or (t[i] in tcharMap and tcharMap[t[i]] != s[i]):
                return False
            
            scharMap[s[i]] = t[i]
            tcharMap[t[i]] = s[i]
            i += 1
        
        return True