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

        # Merge Sort
        def merge(l, m, r, arr):
            left, right = arr[l : m + 1], arr[m + 1 : r + 1]
            i, j, k = 0, 0, l
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i, k = i + 1, k + 1
            
            while j < len(right):
                arr[k] = right[j]
                j, k = j + 1, k + 1


        def mergeSort(l, r, arr):
            if l == r:
                return arr

            m = (r + l) // 2
            mergeSort(l, m, arr)
            mergeSort(m + 1, r, arr)
            merge(l, m, r, arr)

        mergeSort(0, len(nums), nums)

        return nums

        # return nums