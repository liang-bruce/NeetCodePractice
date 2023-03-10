class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # trivial but fast
        # squaredNums = [n * n for n in nums]
        # squaredNums.sort()
        # return squaredNums

        # use minHeap
        # squaredNums = [n * n for n in nums]
        # heapq.heapify(squaredNums)
        # res = []
        # for n in range(len(squaredNums)):
        #     res.append(heapq.heappop(squaredNums))
        # return res

        # 2 ptrs O(n)
        # build the output array in reverse (largest to smallest order)
        res = [0] * len(nums)
        l, r, pos = 0, len(nums) - 1, len(nums) - 1

        while l <= r:
            sqrL, sqrR = nums[l] ** 2, nums[r] ** 2
            if sqrL <= sqrR:
                res[pos] = sqrR
                pos, r = pos - 1, r - 1
            else:
                res[pos] = sqrL
                pos, l = pos - 1, l + 1
        
        return res
