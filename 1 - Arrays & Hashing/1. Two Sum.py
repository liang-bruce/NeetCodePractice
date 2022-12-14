class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}

        # using enumerator: 53 & 9
        # for i in range(len(nums)):
        #     currComplement = target - nums[i]
        #     if nums[i] in complementMap:
        #         return [i, complementMap[nums[i]]] 
        #     else:
        #         complementMap[currComplement] = i

        # using enumerator: 62 & 14
        for i,n in enumerate(nums):
            currComplement = target - n
            if n in complementMap:
                return [i, complementMap[n]] 
            else:
                complementMap[currComplement] = i