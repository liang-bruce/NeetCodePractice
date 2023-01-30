from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman-ford Algo - use 2 arrays (1 is temp)
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tempPrices = prices.copy()

            for s, d, c in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + c < tempPrices[d]:
                    tempPrices[d] = prices[s] + c
            
            prices = tempPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]

        #bfs - TLE
        # construct adjList
        # adjList = {i:[] for i in range(n)}
        # for s, d, c in flights:
        #     adjList[s].append([c, d])
        
        # q = deque()
        # q.append([0, src])
        # visited = set()
        # stop = 0
        # res = float('inf')

        # while stop <= k + 1:
        #     for _ in range(len(q)):
        #         curCost, curNode = q.popleft()
        #         if curNode == dst:
        #             res = min(res, curCost)
        #         if curNode in visited:
        #             continue
        #         for c, d in adjList[curNode]:
        #             if d not in visited:
        #                 q.append([c + curCost,d])

        #     stop += 1
        
        # return -1 if res == float('inf') else res