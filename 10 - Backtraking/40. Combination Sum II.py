class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2^n) NP complete
        # sort the list to help skip identical candidate
        candidates.sort()

        res = []

        def backtrack(cur, pos, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or pos >= len(candidates):
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                # print(cur)
                backtrack(cur, i + 1, total + candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, 0)
        return res

        # TLE but works for small testcases
        # each step make 2 decisions: 1. go to the next index; 2. pop then go to the next index
        # res = set()

        # def dfs(i, cur, total):
        #     if total == target:
        #         comb = cur.copy()
        #         comb.sort()
        #         comb = tuple(comb)
        #         res.add(comb)
        #         return
        #     if i >= len(candidates) or total > target:
        #         return

        #     cur.append(candidates[i])
        #     # print to visualize
        #     print(i, cur, total)
        #     # 1. go to the next;
        #     dfs(i + 1, cur, total + candidates[i])
        #     # 2. pop then go to the next index
        #     cur.pop()
        #     dfs(i + 1, cur, total)

        # dfs(0, [], 0)
        # return res