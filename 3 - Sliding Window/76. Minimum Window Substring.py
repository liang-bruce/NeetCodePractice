class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need 2 hashmap to store counts, 1 for t and 1 for currWindow
        if t == "": return ""

        countT, countWindow = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # need is the unique value in t
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            countWindow[c] = 1 + countWindow.get(c, 0)

            # only when number of uniq number is reached need threshold
            if c in countT and countWindow[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""