class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # O(n^2) TLE
        # l, r = 0, 0
        # res = 0

        # while r < len(nums):
        #     curSum = nums[l]
        #     if curSum == k:
        #         res += 1
        #     while r < len(nums) - 1:
        #         r += 1
        #         curSum += nums[r]
        #         if curSum == k:
        #             res += 1

        #     l , r = l + 1, l + 1
        
        # return res

        # O(n)
        res = 0
        sumCountDict = {0 : 1} # create a dictionary counting the unique subarray with 
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k

            # if there is m subarrays has a sum == diff, it means there is m way to substract them to make current subarray 
            # minus one of them to get subarray's sum ==k
            if diff in sumCountDict:
                res += sumCountDict[diff]

            # update sumCountDict
            sumCountDict[curSum] = sumCountDict.get(curSum, 0) + 1
        
        return res