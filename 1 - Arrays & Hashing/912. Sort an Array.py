class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Heap sort
        # minHeap = nums.copy()
        # heapq.heapify(minHeap)
        # for i in range(len(nums)):
        #     nums[i] = heapq.heappop(minHeap)
        
        # return nums

        # quick sort - TLE for same inputs [1,1,1,,1,1,1,1,1...]
        # def partition(l, r, nums):
        #     pivot = r
        #     i, j = l - 1, l

        #     while j < pivot:
        #         if nums[j] < nums[pivot]:
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]
        #         j += 1
        #     pivotNum = nums.pop(pivot)
        #     nums.insert(i + 1, pivotNum)

        #     return i + 1
        
        # def quickSort(l, r, nums):
        #     if l < r:
        #         pivot = partition(l, r, nums)
        #         # LHS recursion
        #         quickSort(l, pivot - 1, nums)
        #         # RHS recursion
        #         quickSort(pivot + 1, r, nums)
        # random.shuffle(nums)
        # quickSort(0, len(nums) - 1, nums)

        # return nums