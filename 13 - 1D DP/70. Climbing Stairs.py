class Solution:
    def climbStairs(self, n: int) -> int:
        # O(1) space
        if n <= 3:
            return n
        
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            ans = n1 + n2
            n1 = n2
            n2 = ans
            
        
        return ans

        # O(n) space
        # ways = [1,2]

        # if n > 2:
        #     i = 1
        #     while i < n - 1:
        #         ways.append(ways[i] + ways[i-1])
        #         i += 1
        
        # return ways[n - 1]
