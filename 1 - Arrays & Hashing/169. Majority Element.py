class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        limit = len(nums) / 2

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            if count[n] > limit:
                return n

    # O(1) space, Boyer Moore Algo
    # def majorityElement(self, nums: List[int]) -> int:
    #     res, count = 0, 0

    #     for n in nums:
    #         if count == 0:
    #             res = n
    #         count += (1 if n == res else -1)
            
    #     return res