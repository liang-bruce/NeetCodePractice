class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            heapq.heappush(maxHeap, [-dist, x, y]) #python default heapify by the first element
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for dist, x, y in maxHeap:
            res.append([x, y])
        return res

        #  min heap
        # pts = []
        # for x, y in points:
        #     dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
        #     pts.append([dist, x, y]) #python default heapify by the first element

        # res = []
        # heapq.heapify(pts)
        # # print(pts)
        # for i in range(k):
        #     dist, x, y = heapq.heappop(pts) # pop k smallest element
        #     res.append([x, y])
        # return res
