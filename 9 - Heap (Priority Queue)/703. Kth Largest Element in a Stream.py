class KthLargest:
    # use minHeap with size K to store only the largest K element, return minHeap[0] for the Kth largest element
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = [n for n in nums]
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # if added for edge case - initial array length < k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]