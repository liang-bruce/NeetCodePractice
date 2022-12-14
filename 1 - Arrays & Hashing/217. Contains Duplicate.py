class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            else:
                numsSet.add(num)
        return False

        # slow pythonic way, need to convert the whole list to set
        # setLength = len(set(nums))
        # if setLength == len(nums):
        #     return False
        # return True