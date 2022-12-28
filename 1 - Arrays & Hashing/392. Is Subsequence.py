class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        
        while i >=0 and j >= 0:
            currS = s[i]
            currT = t[j]

            if currS == currT:
                i -= 1
                j -= 1
                s = s[:-1]
            else:
                j -= 1
        
        return True if len(s) == 0 else False