class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # each step make 2 decisions: 1. go with same index; 2. pop then go to the next index
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            # print to visualize
            # print(i, cur, total)
            # 1. go with same index;
            dfs(i, cur, total + candidates[i])
            # 2. pop then go to the next index
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res