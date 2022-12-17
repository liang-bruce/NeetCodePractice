class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            # update freqMap
            freqMap[s[right]] = 1 + freqMap.get(s[right], 0)

            # shift left border to the right when K operation is not enough to make the result better
            while (right - left + 1) - max(freqMap.values()) > k:
                freqMap[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result
