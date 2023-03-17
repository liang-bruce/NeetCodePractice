class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # res = [0] * 2 * len(nums)
        # for i in range(len(res)):
        #     res[i] = nums[i % len(nums)]
        
        # return res

        # res = []
        # lenNum = len(nums)
        # for i in range(2 * lenNum):
        #     res.append(nums[i % lenNum])
        
        # return res

        # lenNum = len(nums)
        # res = [0] * 2 * lenNum
        # res[:lenNum + 1] = nums
        # res[lenNum:] = nums
        # return res

        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans