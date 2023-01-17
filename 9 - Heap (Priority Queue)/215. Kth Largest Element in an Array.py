class Solution:
    # O(nlogK) good for large N small k - minHeap with size k
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     minHeap = []
    #     for n in nums:
    #         heapq.heappush(minHeap, n)

    #         if len(minHeap) > k:
    #             heapq.heappop(minHeap)
        
    #     return heapq.heappop(minHeap)
    
    # O(n) average & O(n^2) worst - quick select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        targetIndex = len(nums) - k

        def quickSelect(l,r):
            pivot, tracker = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[tracker], nums[i] = nums[i], nums[tracker]
                    tracker += 1
            
            nums[tracker], nums[r] = nums[r], nums[tracker]
            if tracker == targetIndex:
                return nums[targetIndex]
            elif tracker > targetIndex:
                return quickSelect(l, tracker - 1)
            else:
                return quickSelect(tracker + 1, r)
        
        return quickSelect(0, len(nums) - 1)