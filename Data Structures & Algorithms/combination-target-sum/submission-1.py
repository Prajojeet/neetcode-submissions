class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def bt_dfs(path, summ, index):
            # Base Case
            if summ > target:
                return

            # Base Case equity
            if summ == target:
                ans.append(path[:])
                return

            for i in range(index, len(nums)):
                summ += nums[i]
                path.append(nums[i])
                bt_dfs(path, summ, i)
                summ -= nums[i]
                path.pop()

        bt_dfs([], 0, 0)
        return ans
