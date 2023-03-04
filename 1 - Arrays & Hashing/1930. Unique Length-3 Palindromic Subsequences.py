class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        res = set()


        for m in range(len(s)):
            right[s[m]] -= 1
            if right[s[m]] == 0:
                right.pop(s[m])
            
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[m], c))
            
            left.add(s[m])
        
        return len(res)