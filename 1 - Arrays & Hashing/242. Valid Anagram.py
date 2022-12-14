class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # build a map for s counting occurence of char
        sMap = {}
        for char in s:
            if char in sMap:
                sMap[char] += 1
            else:
                sMap[char] = 1
        
        # build a map for t counting occurence of char
        tMap = {}
        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1
        
        # validating anagram
        if len(sMap.keys()) != len(tMap.keys()):
            return False
             
        for key, value in sMap.items():
            if not key in tMap:
                return False
            if tMap[key] != value:
                return False
        return True