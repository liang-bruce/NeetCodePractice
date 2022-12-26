class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # construct a max heap O(nlogn)
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -1 * s)
        
        # keep popping and comparing O(n)
        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap) * -1
            stone2 = heapq.heappop(maxHeap) * -1

            if stone1 > stone2:
                newStone = stone1 - stone2
                heapq.heappush(maxHeap, -newStone)
            # no need to check cos 1 always larger than 2
            # elif stone1 < stone2:
            #     newStone = stone2 - stone1
            #     heapq.heappush(maxHeap, -newStone)

        return maxHeap[0] * -1 if len(maxHeap) > 0 else 0