class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create 3 hashMaps roe row, col & blks to store seen value
        # blks are (0,0) (0,1) (0,2) etc, r//3, c//3
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blks = collections.defaultdict(set)

        # O(n), loop once only and store seen values in 3 hashmaps if not seen
        for r in range(len(board)):
            for c in range(len(board)):
                ele = board[r][c]
                
                if ele != ".":
                    if (ele in rows[r] or
                        ele in cols[c] or
                        ele in blks[(r // 3 , c // 3)]):
                        return False
                    else:
                        rows[r].add(ele)
                        cols[c].add(ele)
                        blks[(r // 3, c // 3)].add(ele)
        
        return True