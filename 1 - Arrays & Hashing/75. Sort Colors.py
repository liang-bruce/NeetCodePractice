class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             tmp = nums[i]
        #             nums[i] = nums[j]
        #             nums[j] = tmp
        
        # bucket sort
        bucket = [0, 0, 0]

        for i in range(len(nums)):
            num = nums[i]
            bucket[num] += 1

        i, j = 0, 0
        while i < len(bucket):
            size = bucket[i]
            while size > 0:
                nums[j] = i
                size, j = size - 1, j + 1
            i += 1

        # 2 ptr + partition (1 pass algo)
        # low = 0
        # high = len(nums) - 1
        # mid = 0

        # while mid <= high:
        #     if nums[mid] == 0:
        #         nums[low], nums[mid] = nums[mid], nums[low]
        #         low += 1
        #         mid += 1
        #     elif nums[mid] == 1:
        #         mid +=1
        #     else:
        #         nums[mid], nums[high] = nums[high], nums[mid]
        #         high -= 1
        # return nums