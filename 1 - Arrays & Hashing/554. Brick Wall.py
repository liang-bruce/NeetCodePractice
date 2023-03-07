class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # ROW = len(wall)
        
        # # use prefix sum
        # prefixWall = []
        # maxCol = 0
        # for r in range(ROW):
        #     prefixWall.append([])
        #     curSum = 0
        #     for c in range(len(wall[r]) - 1):
        #         curSum += wall[r][c]
        #         prefixWall[r].append(curSum)
        #     maxCol = max(maxCol, len(wall[r]))

        # # print(prefixWall)
        # # use a hashmap to 
        # gapCounter = {0 : 0}
        # for r in prefixWall:
        #     for gap in r:
        #         gapCounter[gap] = gapCounter.get(gap, 0) + 1
        
        # return ROW - max(gapCounter.values())
        
        # in one go
        ROW = len(wall)
        counter = {0 : 0}

        for row in wall:
            curGap = 0
            for brick in range(len(row) - 1):
                curGap += row[brick]
                counter[curGap] = counter.get(curGap, 0) + 1
        
        return ROW - max(counter.values())