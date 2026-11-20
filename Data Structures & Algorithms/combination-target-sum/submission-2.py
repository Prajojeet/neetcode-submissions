class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def bt_dfs(path, summ, poi):
            if summ > target:
                return

            if summ == target:
                res.append(path[:])

            for i in range(poi, len(nums)):
                summ += nums[i]
                path.append(nums[i])
                bt_dfs(path, summ, i)
                path.pop()
                summ -= nums[i]
        bt_dfs([], 0, 0)
        return res