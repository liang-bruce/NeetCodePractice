class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return helper(s, i + 1, j) or helper(s, i, j - 1)
        
        return True  