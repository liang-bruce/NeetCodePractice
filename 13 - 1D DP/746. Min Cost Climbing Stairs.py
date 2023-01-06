class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #use a dict to store the index: minCost pair
        stepMinCost = {len(cost) - 1: cost[-1], len(cost) - 2: min(cost[-1]+ cost[-2], cost[-2])}

        # loop backwards to compute minCost of each step
        for i in range(len(cost) - 3, -1, -1):
            stepMinCost[i] = min(cost[i] + stepMinCost[i + 1], cost[i] + stepMinCost[i + 2])

        return min(stepMinCost[0], stepMinCost[1])