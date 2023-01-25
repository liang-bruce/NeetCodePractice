class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lSum = 0

        for i in range(len(nums)):
            rSum = total - lSum - nums[i]
            if rSum == lSum:
                return i
            
            lSum += nums[i]
        
        return -1



        # this doesn't work for cases like [-1,-1,-1,-1,-1,0]
        # while l <= r:
        #     if lSum > rSum:
        #         rSum += nums[r]
        #         r -= 1
        #     elif lSum < rSum:
        #         lSum += nums[l]
        #         l += 1
        #     else:
        #         return l
        
        # return -1