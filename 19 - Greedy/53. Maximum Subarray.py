class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n), O(n)
        # N = len(nums)
        # curMax = [nums[0]] * N
        # for i in range(1, N):
        #     curMax[i] = max(nums[i] + curMax[i - 1], nums[i])

        # return max(curMax)

        # O(n), O(1)
        res = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(res, curSum)
        
        return res