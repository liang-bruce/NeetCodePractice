class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        curSum = 0

        while r < len(nums):
            curSum += nums[r]
            # valid subarray
            while l <= r and curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
            
            r += 1
            
        return res if res != float('inf') else 0