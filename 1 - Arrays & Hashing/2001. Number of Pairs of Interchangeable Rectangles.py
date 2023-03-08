class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        def getNumOfPairs(num):
            pairs = 0
            for i in range(num):
                pairs += i
            return pairs
        
        # seen = {} # spped up using memoization
        # ratios = []
        # for rectangle in rectangles:
        #     ratios.append(rectangle[0] / rectangle[1])
        
        # ratios.sort()

        # print(ratios)
        # l, r, res = 0, 0, 0
        # while r < len(ratios):
        #     counter = 0
        #     # print(f"outer loop {l, r}")
        #     while r < len(ratios) and ratios[r] == ratios[l]:
        #         counter += 1
        #         r += 1
        #         # print(f"    inner loop {l, r}")
        #     if counter not in seen:
        #         seen[counter] = getNumOfPairs(counter)

        #     res += seen[counter]

        #     l = r
        
        # return res

        # actually the order does not matter
        ratios = {}
        for rectangle in rectangles:
            ratio = rectangle[0] / rectangle[1]
            ratios[ratio] = ratios.get(ratio, 0) + 1
        
        res = 0
        for ratio, num in ratios.items():
            res += getNumOfPairs(num)
        
        return res
