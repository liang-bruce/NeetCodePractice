class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        def palinHelper(l, r):
            nonlocal counter
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # for odd length
            palinHelper(i, i)

            # for even length
            palinHelper(i, i + 1)
        
        return counter