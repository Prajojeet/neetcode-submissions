class Solution:
    def __init__(self):
        self.result=[]

    def bt_dfs(self, path, counter):
        # Append the list to result
        self.result.append(path[:])
        
        # One edge case for the leaf
        if len(path)==len(self.nums):
            return
        
        for i in range(len(self.nums)):
            if counter<i:
                counter+=1
                path.append(self.nums[i])
                self.bt_dfs(path,counter)
                path.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start the counter with -1
        self.nums=nums
        self.bt_dfs([],-1)
        return self.result