class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n^2) is to brute force it using 2 for loops
        # this is O(n), one pointer travelling from 0 and one from the right most, keep moving smaller ptrs 
        left, right = 0, len(height) - 1
        maxV = 0
        
        while left < right:
            currV = min(height[left], height[right]) * (right - left)
            maxV = max(maxV, currV)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxV