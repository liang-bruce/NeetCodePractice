class NumArray:

    # O(n^2)
    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     res = 0
    #     for i in range(left, right + 1):
    #         res += self.nums[i]
    #     return res
    # -2, -2, 1, -4, -2, -3

    # O(n) range sum (prefix)
    def __init__(self, nums: List[int]):
        self.runningSum = [nums[0]]
        for i in range(1, len(nums)):
            self.runningSum.append(nums[i] + self.runningSum[-1])

    def sumRange(self, left: int, right: int) -> int:
        r = self.runningSum[right]
        l = self.runningSum[left - 1] if left > 0 else 0
        return r - l