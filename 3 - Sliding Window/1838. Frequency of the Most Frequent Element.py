class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort the array because we are only allowed to increase elements
        # expand to right only when it is possible to get len(window) same elements (nums[r]*len(window) <= curSum + k)
        
        nums.sort()
        l, r = 0, 0
        curSum, res = 0, 0

        while r < len(nums):
            curSum += nums[r]
            # while the window is invalid, shrink from left
            while nums[r] * (r - l + 1) > curSum + k:
                curSum -= nums[l]
                l += 1
            
            # now window is valid, record length and expand to right
            res = max(res, r - l + 1)
            r += 1 

        return res