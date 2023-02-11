class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1

        for i in range(1, len(nums)):
            cur, pre = nums[i], nums[i - 1]
            if pre != cur:
                nums[pos] = cur
                pos += 1
        return pos