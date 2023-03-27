class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        curSum = 0
        validSum = threshold * k
        res = 0

        while l <= len(arr) - k + 1 and r < len(arr):
            while r - l < k and r < len(arr):
                curSum += arr[r]
                r += 1
            # print(l, r, curSum, validSum)
            if curSum >= validSum:
                res += 1
            curSum -= arr[l]
            l += 1
        
        return res