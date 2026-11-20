class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)

        def bt_dfs(i, path, summ):
            if summ == target:
                res.append(path.copy())
                return

            if summ > target or i >= len(candidates):
                return
            
            # Consider the element in the iteration
            path.append(candidates[i])
            bt_dfs(i + 1, path, summ + candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
            bt_dfs(i + 1, path, summ)

        bt_dfs(0, [], 0)
        return res