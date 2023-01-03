class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for row index
        m = len(matrix)
        n = len(matrix[0]) - 1
        leftRow = 0
        rightRow = len(matrix) - 1
        targetRow = -1
        
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            if target >= matrix[midRow][0] and target <= matrix[midRow][n]:
                targetRow = midRow
                break
            if target > matrix[midRow][n]:
                leftRow = midRow + 1
            if target < matrix[midRow][0]:
                rightRow = midRow - 1

        # return false if target not in range
        if targetRow == -1:
            return False

        # binary search on the targetRow
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[targetRow][mid]:
                return True
            if target > matrix[targetRow][mid]:
                l = mid + 1
            if target < matrix[targetRow][mid]:
                r = mid - 1 
        return False
