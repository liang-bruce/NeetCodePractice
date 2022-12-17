class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        start = 0
        result = 0
        
        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            result = max(result, end - start + 1)
        
        return result
        
        # if (len(s)<1):
        #     return len(s)
        # start, end = 0, 1
        # maxLen = 1
        # while start < len(s) and end < len(s):
        #     seenChar = set()
        #     if s[start] != s[end]:
        #         seenChar.add(s[start])
        #         while end < len(s) and s[end] not in seenChar:
        #             seenChar.add(s[end])
        #             end += 1
        #         currLen = len(seenChar)
        #     else:
        #         currLen = 1

        #     start += 1
        #     end = start + 1
        #     maxLen = max(maxLen, currLen)
        
        # return maxLen
            