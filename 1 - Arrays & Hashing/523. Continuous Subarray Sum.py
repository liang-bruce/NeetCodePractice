class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # use a hashmap {mod: firstIndex} to store mod values
        # initialize it with {0:-1} to avoid edge case: nums[0] satisfies condition

        modMap = {0: -1}
        curSum = 0

        for i, n in enumerate(nums):
            curSum += n
            curMod = curSum % k
            if curMod not in modMap:
                modMap[curMod] = i
            elif i - modMap[curMod] >= 2:
                return True