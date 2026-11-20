class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt_dfs(path, poi):
            res.append(path[:])

            if len(path) == len(nums):
                return

            for i in range(poi + 1, len(nums)):
                path.append(nums[i])
                bt_dfs(path, i)
                path.pop()

        bt_dfs([], -1)
        return res