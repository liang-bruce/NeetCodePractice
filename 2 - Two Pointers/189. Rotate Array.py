class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # extra O(n) memory
        # shift = k % len(nums)
        # helper = [0] * shift 
        # i = 0
        # while i < len(nums) - shift:
        #     helper.append(nums[i])
        #     i += 1
        
        # j = 0
        # while j < shift:
        #     helper[j] = nums[i]
        #     i, j = i + 1, j + 1
        
        # for i in range(len(nums)):
        #     nums[i] = helper[i]

        # no extra memory
        # 1. reverse the array
        # 2. reverse first k element
        # 3. reverse second half of reversed array
        
        def reverseArray(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        k = k % len(nums)

        reverseArray(0, len(nums) - 1)
        reverseArray(0, k - 1)
        reverseArray(k, len(nums) - 1)