class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # ROW, COL = len(rooms), len(rooms[0])
        
        # q = deque()
        # visited = set()
        # # put all gate positions in the queue
        # for r in range(ROW):
        #     for c in range(COL):
        #         if rooms[r][c] == 0:
        #             q.append((r, c))
        # dist = 0
        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         if rooms[r][c] == 2147483647:
        #             rooms[r][c] = dist

        #         visited.add((r, c))
        #         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #         for rd, cd in directions:
        #             newR, newC = r + rd, c + cd
        #             if (newR in range(ROW) and newC in range(COL) and
        #                 rooms[newR][newC] == 2147483647 and (newR, newC) not in visited):
        #                 q.append((newR, newC))
        #     dist += 1 
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1