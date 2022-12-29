class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0
        # r = len(nums)

        # while l < r:
        #     m = (l + r) // 2

        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m 

        # return -1

        # recursive:
        def rec(l, r, nums, target):
            if l >= r:
                return -1
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return rec(m + 1, r, nums, target)
            else:
                return rec(l, m, nums, target)
        
        return rec(0, len(nums), nums, target)