import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjList = {i : [] for i in range(n)}
        for i in range(len(edges)):
            edge = edges[i]
            adjList[edge[0]].append([edge[1], succProb[i]]) 
            adjList[edge[1]].append([edge[0], succProb[i]]) 
        
        maxHeap= [[-1, start]] # start with -1 for maxHeap
        visited = set()

        while maxHeap:
            prob, curNode = heapq.heappop(maxHeap)
            visited.add(curNode)
            
            if curNode == end:
                return -prob
            
            for neighbour, probability in adjList[curNode]:
                if neighbour not in visited:
                    heapq.heappush(maxHeap, [-1 * (probability * -prob), neighbour])
        
        return 0