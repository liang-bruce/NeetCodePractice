class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use 2 array recording product of all elements to the left & right of currElement
        # then times leftProduct & rightProduct accordingly
        leftProduct = [1] * (len(nums) + 1)
        rightProduct = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            leftProduct[i+1] = nums[i] * leftProduct[i]
        
        for i in range(len(nums) - 1 , 0, -1):
            rightProduct[i] = nums[i] * rightProduct[i + 1]

        result=[]
        for i in range(len(nums)):
            result.append(leftProduct[i] * rightProduct[i+1])
        
        return result