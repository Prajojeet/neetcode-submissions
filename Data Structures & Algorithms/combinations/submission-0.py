class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def bt_dfs(path, point):
            if len(path)==k:
                ans.append(path[:]) # Python stores mutable references 
                return 
            
            for index in range(n):
                if index>point:
                    path.append(index+1)
                    bt_dfs(path, index)
                    path.pop()
        bt_dfs([],-1)
        return ans