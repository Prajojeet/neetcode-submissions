class Solution:
    def __init__(self):
        self.result=[]
        
    def bt_dfs(self, path,target,counter):
        # Base case to return
        if sum(path)>target:
            return
        # Base Case to append
        if sum(path)==target:
            self.result.append(path[:])
    
        # Recursive case to sum
        for i, num in enumerate(self.nums):
            if counter==i:
                path.append(num)
                self.bt_dfs(path,target,counter)
                path.pop()
            elif counter<i:
                path.append(num)
                counter+=1
                self.bt_dfs(path,target,counter)
                path.pop()
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums=nums
        self.bt_dfs([],target,-1)
        return self.result
