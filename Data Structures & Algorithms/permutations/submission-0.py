# You can't use the same element twice (given unique integers, just pass the hashmap)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def bt_dfs(path, hashmap):
            # Base Case
            if len(nums)==len(path):
                ans.append(path[:])
                return

            for num in nums:
                if num not in hashmap:
                    hashmap.add(num)
                    path.append(num)
                    bt_dfs(path,hashmap)
                    hashmap.discard(num)
                    path.pop()
        bt_dfs([], set())
        return ans