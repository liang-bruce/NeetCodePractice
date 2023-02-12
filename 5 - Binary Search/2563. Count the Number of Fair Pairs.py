class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # think lower <= nums[i] + nums[j] <= upper as 2 conditions
        # 1. sort the array for binary search
        # 2. for each num: 1 * binary search for the lower bound anf 1 * binary search for the upper bound
        # n*log(n)
        
        # First, note that the answer does not change if we sort the array
        nums.sort()
        fairCtr = 0
        for i in range(len(nums)):
            # For each index find the left and right elements for which the sums lie between lower and upper
            l = bisect_left(nums, lower - nums[i])
            r = bisect_right(nums, upper - nums[i])
            fairCtr += (r - l)
            # check if index i lies in the interval, subtract one (we don't want to double count index i) - nums[i] + nums[i] in range
            print(i, l, r, fairCtr)
            if l <= i < r:
                print(i, l, r, -1)
                fairCtr -= 1
        return fairCtr // 2