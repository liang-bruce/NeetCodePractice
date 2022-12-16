class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(nlog(n)) + O(n^2) - O(n^2)
        # sort the array first then for each elemnt perform a 2 sum
        # if use hashmap, space will be O(n)
        # if use 2 ptrs (cos sorted), space will be O(1) 
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            # k for 2 sum is now nums[i]
            currTarget = -nums[i]
            j = i + 1
            k = len(nums) - 1

            # double ptrs for 2 sum 
            while j < k:
                twoSum = nums[j] + nums[k]
                if twoSum < currTarget:
                    j += 1
                if twoSum > currTarget:
                    k -= 1
                if twoSum == currTarget:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # take care of duplicate
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return result