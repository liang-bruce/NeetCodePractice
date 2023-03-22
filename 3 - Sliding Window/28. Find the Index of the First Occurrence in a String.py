class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O(n*m)
        i, j = 0, 0

        while i < len(haystack) and j < len(needle):
            temp = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            
            if j == len(needle):
                return i - j

            i, j = temp + 1, 0
        
        return -1