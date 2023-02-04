class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # sList = s.split(' ')
        # if len(sList) != len(pattern):
        #     return False
        
        # patternMap = {}
        # for i in range(len(sList)):
        #     if pattern[i] not in patternMap:
        #         patternMap[pattern[i]] = sList[i]
        #     else:
        #         if patternMap[pattern[i]] != sList[i]:
        #             return False
        # uniqueVal = set(patternMap.values())

        # return True if len(uniqueVal) == len(patternMap) else False

        #more memo but more intuitive
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True