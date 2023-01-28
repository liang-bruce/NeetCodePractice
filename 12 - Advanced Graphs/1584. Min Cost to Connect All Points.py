import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # setting up graph in adjList
        noOfNode = len(points)
        adjList = {i:[] for i in range(noOfNode)}
        for i in range(noOfNode):
            for j in range(i + 1, noOfNode):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        
        minHeap = [[0, 0]]
        visited = set()
        cost = 0

        while minHeap and len(visited) < noOfNode:
            dist, source = heapq.heappop(minHeap)
            if source in visited:
                continue
            visited.add(source)
            cost += dist
            # print(dist, source)

            for dist, destination in adjList[source]:
                if destination not in visited:
                    heapq.heappush(minHeap, [dist, destination])
        
        return cost