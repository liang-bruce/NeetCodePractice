class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                resTemp, resIndex = stack.pop()
                res[resIndex] = index - resIndex

            stack.append([temp,index])
        return res