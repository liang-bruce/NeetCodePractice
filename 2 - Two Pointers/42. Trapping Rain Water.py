import collections
class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 arrays recording the leftMax and rightMax
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax = [0]
        rightMax = deque([0])
        currLeftMax, currRightMax = 0, 0
        water = 0

        # compute leftMax
        for i in range(1, len(height)):
            currLeftMax = max(height[i - 1], leftMax[i - 1])
            leftMax.append(currLeftMax)
        # compute rightMax
        for i in range(len(height) - 2, -1, -1):
            currRightMax = max(height[i + 1], rightMax[0])
            rightMax.appendleft(currRightMax)
        # compute answer
        for i in range(1, len(height)):
            currWater = min(leftMax[i], rightMax[i]) - height[i] # core logic
            if currWater > 0:
                water += currWater
        
        return water

        # no extra memory - O(1) memo
        # if not height: return 0

        # l, r = 0, len(height) - 1
        # leftMax, rightMax = height[l], height[r]
        # res = 0

        # while l < r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1 
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        
        # return res