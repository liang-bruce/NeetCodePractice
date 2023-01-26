class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        
        for i in range(len(s)):
            # for odd length:
            l, r = i, i
            curPal = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curPal = s[l : r + 1]
                res = curPal if len(curPal) > len(res) else res
                l-= 1
                r += 1

            # for even length:
            l, r = i, i + 1
            curPal = s[l :r + 1]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curPal = s[l : r + 1]
                res = curPal if len(curPal) > len(res) else res
                l -= 1
                r += 1
        
        return res

