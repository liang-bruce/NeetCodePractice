class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        numSet = set()

        for i in range(length):
                numSet.add(i + 1)
        
        for i in nums:
            if i in numSet:
                numSet.remove(i)
        
        res = [i for i in numSet]
        return res
        
        # O(1) Memo solution
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res