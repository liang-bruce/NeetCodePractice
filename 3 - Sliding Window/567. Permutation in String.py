class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # more efficient
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        # initialize matches
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        # start sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
        
        # gap = len(s1) - 1
        # l = 0
        # r = 0 + gap
        # s1Map = {}
        # for c in s1:
        #     # s1Map[c] = (s1Map.count(c) + 1, 0)
        #     if c in s1Map:
        #         s1Map[c] += 1
        #     else:
        #         s1Map[c] = 1
            
        # while r < len(s2):
        #     tempMap = {}

        #     for i in range(l, r + 1):
        #         # print(s2[i])
        #         if s2[i] in s1Map:
        #             if s2[i] in tempMap:
        #                 tempMap[s2[i]] += 1
        #             else:
        #                 tempMap[s2[i]] = 1
                
        #     l += 1
        #     r = l + gap

        #     # print(tempMap, s1Map)
        #     if tempMap == s1Map:
        #         return True
        
        # return False