class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # when array length can be change only
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == val:
        #         temp = nums[-1]
        #         nums[-1] = nums[i]
        #         nums[i] = temp

        #         nums.pop()
        
        # return len(nums)

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k