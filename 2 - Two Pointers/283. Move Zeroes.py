class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n^2)
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == 0:
        #         j = i + 1
        #         while j < len(nums) - 1 and nums[j] == 0:
        #             j += 1
        #         temp = nums[i]
        #         nums[i] = nums[j]
        #         nums[j] = temp 
        #     i += 1
        
        # O(n) with extra memo
        # nonZeros = []
        # for n in nums:
        #     if n != 0:
        #         nonZeros.append(n)
        # i= 0
        # while i < len(nonZeros):
        #     nums[i] = nonZeros[i]
        #     i += 1
        # while i < len(nums):
        #     nums[i] = 0
        #     i += 1

        # O(n) with no extra memo
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1