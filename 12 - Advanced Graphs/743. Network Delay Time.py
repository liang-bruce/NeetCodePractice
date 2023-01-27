import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # full Dijsktra Algo
        # timeMap = {n:[] for n in range(n + 1)}
        # for source, dest, time in times:
        #     timeMap[source].append([dest, time])
        
        # shortest = {}
        # minHeap = [[0, k]]
        
        # while minHeap:
        #     time1, node1 = heapq.heappop(minHeap)
        #     if node1 in shortest:
        #         continue
        #     shortest[node1] = time1

        #     for node2, time2 in timeMap[node1]:
        #         if node2 not in shortest:
        #             heapq.heappush(minHeap,[time1 + time2, node2])
        
        # if len(shortest) < n:
        #     return -1
        # return max(shortest.values())

        # only time Dijsktra
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1