class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part, res = [], []

        def dfs(pos):
            if pos >= len(s):
                res.append(part.copy())
                return
            
            for i in range(pos, len(s)):
                if self.isPalindrome(s, pos, i):
                    part.append(s[pos : i + 1])
                    dfs(i + 1)
                    part.pop()
        
        dfs(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True