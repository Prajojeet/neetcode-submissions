class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        def bt_dfs(path, hashmap):
            # Base Case
            if len(nums)==len(path):
                ans.add(tuple(path[:]))
                return

            for index, num in enumerate(nums):
                if index not in hashmap:
                    hashmap.add(index)
                    path.append(num)
                    bt_dfs(path,hashmap)
                    hashmap.discard(index)
                    path.pop()
        bt_dfs([], set())
        output = [list(item) for item in ans]
        return output