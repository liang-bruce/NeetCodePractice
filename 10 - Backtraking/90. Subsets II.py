class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res, subset = [], []

        def backtracking(pos):
            if pos == len(nums):
                res.append(subset.copy())
                print(subset)
                return

            subset.append(nums[pos])

            # include nums[pos]
            backtracking(pos + 1)

            # not include nums[pos] & skipping same element
            subset.pop()
            while pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
                pos += 1
            backtracking(pos + 1)
            return 
        
        backtracking(0)
        return res