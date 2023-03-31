class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos, dupCount = 1, 1

        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pos] = nums[i]
                pos += 1
                dupCount = 1
            else:
                if dupCount < 2:
                    nums[pos] = nums[i]
                    pos += 1
                dupCount += 1
        
        return pos