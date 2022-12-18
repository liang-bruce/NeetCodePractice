class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = sys.maxsize

        # binary search
        while l <= r:
            mid = (l + r) // 2
            minNum = min(minNum, nums[mid])

            # minNum is on the RHS
            if nums[r] < nums[mid]:
                l = mid + 1
            
            #minNum is on the LHS
            else:
                r = mid - 1
        
        return minNum