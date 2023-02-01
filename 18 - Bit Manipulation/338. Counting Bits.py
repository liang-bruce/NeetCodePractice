class Solution:
    def countBits(self, n: int) -> List[int]:
        # helper function to get noOfOnes:
        def noOfOne(num):
            counter = 0

            while num > 0:
                if num & 1 == 1:
                    counter += 1
                num = num >>1
            return counter
        
        res = []
        for i in range(n + 1):
            res.append(noOfOne(i))
        
        return res

    # # below is a dp way to solve this problem, but it is hard to understand
    # def countBits(self, n: int) -> List[int]:
    #     dp = [0] * (n + 1)
    #     offset = 1

    #     for i in range(1, n + 1):
    #         if offset * 2 == i:
    #             offset = i
    #         dp[i] = 1 + dp[i - offset]
    #     return dp