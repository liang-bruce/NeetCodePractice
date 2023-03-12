class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 1. find the subarray satistying condition
        # 2. reduce the length from left until condition is not met
        # 3. expand window to the right until condition is met again
        # iterate until the end of array

        l, oddCount, subCount, res = 0, 0, 0, 0
        
        for r in range(len(nums)):
            # expand to right
            if nums[r] % 2 == 1:
                oddCount += 1
                subCount = 0
            
            # shrink from left
            while oddCount == k:
                if nums[l] % 2 == 1:
                    oddCount -= 1
                l += 1
                subCount += 1
                # for each r is not odd afterwards, there are [subCount] subarray added
                # draw to visualize
            res += subCount
            

        return res