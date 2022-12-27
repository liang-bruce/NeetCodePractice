class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # O(1) space and O(n)time
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i],rightMax)
            arr[i] = rightMax
            rightMax = newMax
        
        return arr
        # O(n) space and O(2n)time
        # currMax = -1
        # maxMap = {}

        # for i in range(len(arr) - 1, -1, -1):
        #     if (i + 1) == len(arr):
        #         maxMap[i] = currMax
        #     else:
        #         currMax = max(currMax, arr[i+1])
        #         maxMap[i] = currMax
        
        # for i in range(len(arr)):
        #     arr[i] = maxMap[i]
        
        # return arr