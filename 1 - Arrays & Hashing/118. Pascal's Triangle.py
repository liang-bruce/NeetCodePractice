class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res = []
        # for i in range(numRows):
        #     currRow = [1] * (i + 1)
        #     if i >= 2:
        #         prevRow = res[i-1]
        #         for j in range(1, i):
        #             currRow[j] = prevRow[j-1] + prevRow[j] 
        #     res.append(currRow)
        # return res

        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res