class Solution:
    def rob(self, nums: List[int]) -> int:
        numsLen = len(nums)
        currMax = {numsLen - 1 : nums[numsLen - 1], numsLen - 2 : max(nums[numsLen - 2], nums[numsLen - 1])}

        for i in range(len(nums) - 3, -1, -1):
            currMax[i] = max(nums[i] + currMax[i + 2], currMax[i + 1])

        return currMax[0] 
    
    # NeetCode:
    # def rob(self, nums: List[int]) -> int:
    #     rob1, rob2 = 0, 0

    #     for n in nums:
    #         temp = max(n + rob1, rob2)
    #         rob1 = rob2
    #         rob2 = temp
    #     return rob2